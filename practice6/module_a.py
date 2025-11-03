# practice6/module_a.py
# ~60 строк — в этом файле есть VERSION маркер в первой строке,
# который мы будем менять в разных ветках чтобы получить конфликты.

VERSION = "v0"  # <<< EDIT_THIS_LINE_IN_BRANCH

import math
import random
from typing import List

class Vec:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vec") -> "Vec":
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec") -> "Vec":
        return Vec(self.x - other.x, self.y - other.y)

    def scale(self, factor: float) -> "Vec":
        return Vec(self.x * factor, self.y * factor)

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vec({self.x:.2f}, {self.y:.2f})"

def random_vecs(n: int, scale: float = 10.0) -> List[Vec]:
    return [Vec(random.uniform(-scale, scale), random.uniform(-scale, scale)) for _ in range(n)]

def centroid(vecs: List[Vec]) -> Vec:
    if not vecs:
        return Vec(0, 0)
    sx = sum(v.x for v in vecs)
    sy = sum(v.y for v in vecs)
    return Vec(sx/len(vecs), sy/len(vecs))

class PointCluster:
    def __init__(self, points: List[Vec]):
        self.points = points

    def center(self) -> Vec:
        return centroid(self.points)

    def farthest(self) -> Vec:
        c = self.center()
        return max(self.points, key=lambda p: (p - c).length())

    def bounding_box(self):
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        return {"min": Vec(min(xs), min(ys)), "max": Vec(max(xs), max(ys))}

def cluster_demo(n: int = 10):
    pts = random_vecs(n)
    c = PointCluster(pts)
    print("Points:", pts)
    print("Center:", c.center())
    print("Farthest:", c.farthest())
    print("Bounding box:", c.bounding_box())

if __name__ == "__main__":
    cluster_demo(25)
    
