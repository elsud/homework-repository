import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_of_slow_calculate(n: int = 500) -> int:
    """Calculating total sum of slow_calculate of all numbers starting from 0 to n."""
    with Pool(n) as p:
        return sum(p.map(slow_calculate, range(n)))
