import multiprocessing
from multiprocessing import Manager, Process


def worker(d, key, value):
    d[key] = value
    print("key=%s value=%s" % (key, value))


if __name__ == "__main__":
    mgr = Manager()
    d = mgr.dict()
    jobs = [Process(target=worker, args=(d, i, i*i)) for i in range(10)]

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print(d)
