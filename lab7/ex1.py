import concurrent.futures
import time
import os

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    result = count(x)
    print("[pid=%s]" % os.getpid() + "item=%s" % x + " result=%s" % result)


def count(number):
    for i in range(0, 10000000):
        i = i + 1
    return i * number


if __name__ == "__main__":
    start_time = time.perf_counter()
    for x in lst:
        evaluate_item(x)
    print("secvential time=%s seconds" % (time.perf_counter() - start_time))

    start_time_1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for x in lst:
            executor.submit(evaluate_item, x)
    print("thread pool time=%s seconds" % (time.perf_counter()-start_time_1))

    start_time_2 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for x in lst:
            executor.submit(evaluate_item, x)
    print("process pool time=%s seconds" % (time.perf_counter() - start_time_2))
