import multiprocessing
import time
import os


def sq(x):
    print("[%s] x=%s" % (os.getpid(), x))
    time.sleep(2)
    return x * x


if __name__ == "__main__":
    lst = list(range(40))
    pool = multiprocessing.Pool(processes=4)
    rez = pool.map(sq, lst)
    pool.close()
    pool.join()
    print(rez)
