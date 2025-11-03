# practice6/module_b.py
VERSION = "v0"  # <<< EDIT_THIS_LINE_IN_BRANCH

import time
from functools import wraps
from typing import Iterable, Callable, Generator, Any, List

def timing(f: Callable) -> Callable:
    @wraps(f)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"{f.__name__} took {end-start:.6f}s")
        return result
    return wrapped

def chunked(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) >= size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

@timing
def process_numbers(nums):
    s = 0
    for chunk in chunked(nums, 10):
        s += sum(x*x for x in chunk)
    return s

def sliding_window(seq, k):
    it = iter(seq)
    window = []
    for x in it:
        window.append(x)
        if len(window) > k:
            window.pop(0)
        if len(window) == k:
            yield list(window)

def map_pipeline(data, funcs):
    res = data
    for fn in funcs:
        res = map(fn, res)
    return list(res)

def demo_pipeline():
    nums = list(range(100))
    print("Process numbers result:", process_numbers(nums))
    print("Sliding windows length 5 example:", len(list(sliding_window(nums, 5))))
    print("Chunked example:", list(chunked(nums, 15))[:2])
    print("Pipeline doubled sample:", map_pipeline(nums[:10], [lambda x: x*2, lambda x: x+1])[:5])

if __name__ == "__main__":
    demo_pipeline()
