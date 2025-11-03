# practice6/module_c.py
VERSION = "v0"  # <<< EDIT_THIS_LINE_IN_BRANCH

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import itertools
import random

_id_counter = itertools.count(1)

@dataclass
class Record:
    id: int
    name: str
    value: float
    tags: List[str] = field(default_factory=list)

class InMemoryDB:
    def __init__(self):
        self._data: Dict[int, Record] = {}

    def create(self, name: str, value: float, tags: Optional[List[str]] = None) -> Record:
        rid = next(_id_counter)
        rec = Record(id=rid, name=name, value=value, tags=tags or [])
        self._data[rid] = rec
        return rec

    def get(self, rid: int) -> Optional[Record]:
        return self._data.get(rid)

    def update(self, rid: int, **kwargs) -> Optional[Record]:
        rec = self._data.get(rid)
        if not rec:
            return None
        for k, v in kwargs.items():
            if hasattr(rec, k):
                setattr(rec, k, v)
        return rec

    def delete(self, rid: int) -> bool:
        if rid in self._data:
            del self._data[rid]
            return True
        return False

    def query_by_tag(self, tag: str) -> List[Record]:
        return [r for r in self._data.values() if tag in r.tags]

def demo_db():
    db = InMemoryDB()
    a = db.create("alpha", 1.23, ["x", "y"])
    b = db.create("beta", 4.56, ["y"])
    c = db.create("gamma", 7.89, ["z"])
    print("All:", list(db._data.values()))
    db.update(a.id, value=2.0)
    print("After update:", db.get(a.id))
    print("By tag y:", db.query_by_tag("y"))
    db.delete(b.id)
    print("After delete:", list(db._data.values()))

if __name__ == "__main__":
    demo_db()
