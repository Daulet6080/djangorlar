from django.db import models
from django.utils import timezone

class SoftDeletableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class AbstractSoftDeletableModel(models.Model):
    is_deleted=models.BooleanField(default=False,db_index=True)
    deleted_at=models.DateTimeField(null=True,blank=True)
    objects=SoftDeletableManager()
    all_objects=AllObjectsManager()
    class Meta:
        abstract=True
    
    def delete(self,using=None,keep_parents=False):
        if not self.is_deleted:
            self.is_deleted=True
            self.deleted_at=timezone.now()
            self.save(update_fields=["is_deleted","deleted_at"])
            
    def hard_delete(self,using=None,keep_parents=False):
        super().delete(using=using,keep_parents=keep_parents)
        
    def restore(self):
        if self.is_deleted:
            self.is_deleted=False
            self.deleted_at=None
            self.save(update_fields=["is_deleted","deleted_at"])