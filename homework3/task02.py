"""
Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function."""
import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def do():
    """Calculating total sum of slow_calculate() of all numbers starting from 0 to 500"""
    # How fast the program works:
    # start = time.time()
    # (str(int(time.time() - start) // 60) + ":" + str(int((time.time() - start) * 10) % 60))
    # For knowing how many cores you have:
    # multiprocessing.cpu_count()
    with Pool() as p:
        return sum(p.map(slow_calculate, range(501)))


# for running in this file:
# if __name__ == "__main__":
#     print(do())
