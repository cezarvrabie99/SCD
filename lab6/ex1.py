import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime
from random import randint


def test_with_barrier(syncronizer, locker):
    name = multiprocessing.current_process().name
    t = randint(1, 10)
    sleep(t)
    syncronizer.wait()
    now = time()
    with locker:
        print("process %s --->[%s] %s" % (name, t, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    t = randint(1, 10)
    sleep(t)
    now = time()
    print("process %s --->[%s] %s" % (name, t, datetime.fromtimestamp(now)))


if __name__ == "__main__":
    syncronizer = Barrier(2)
    locker = Lock()

    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(syncronizer, locker)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(syncronizer, locker)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
