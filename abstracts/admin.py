from django.contrib import admin

def soft_delete_selected(modeladmin,request,queryset):
    for obj in queryset:
        obj.delete()
    modeladmin.message_user(request,"Выбранные обьекты мягко удалены.")

def restore_selected(modeladmin,request,queryset):
    for obj in queryset:
        obj.restore()
    modeladmin.message_user(request,"Выбранные обьекты  восстановлены.")
    
def hard_delete_selected(modeladmin,request,queryset):
    for obj in queryset:
        obj.hard_delete()
    modeladmin.message_user(request,"Выбранные обьекты  удалены навсегда.")
    
class SoftDeleteAdmin(admin.ModelAdmin):
    list_display=("__str__","is_deleted","deleted_at")
    list_filter=("is_deleted",)
    actions=[soft_delete_selected,restore_selected,hard_delete_selected]
    
    def get_queryset(self, request):
        return super.model.all_objects.get_queryset()