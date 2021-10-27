import threading

res1 = 0
res2 = 0
counter = 1000000
my_lock = threading.Lock()


def increment_with_lock():
    global res1
    for i in range(counter):
        my_lock.acquire()
        res1 += 1
        my_lock.release()
    print("lck_inc. res1=%s" % res1)


def decrement_with_lock():
    global res1
    for i in range(counter):
        my_lock.acquire()
        res1 -= 1
        my_lock.release()
    print("lck_dec. res1=%s" % res1)


def increment_without_lock():
    global res2
    for i in range(counter):
        res2 += 1
    print("inc. res2=%s" % res2)


def decrement_without_lock():
    global res2
    for i in range(counter):
        res2 -= 1
    print("dec. res2=%s" % res2)


if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("final. res1=%s" % res1)
    print("final. res2=%s" % res2)
