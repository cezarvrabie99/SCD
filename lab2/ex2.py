import threading
import time


class Box():
    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


def adder(box, items):
    while items > 0:
        print("add 1 item\n")
        box.add()
        items -= 1


def remover(box, items):
    while items > 0:
        print("remove 1 item\n")
        box.remove()
        items -= 1


if __name__ == "__main__":
    items = 5000
    print("will add %s in the box" % items)
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("%s items still in the box" % box.total_items)

    items = 10
    print("will add %s in the second box" % items)
    box2 = Box()
    tt1 = threading.Thread(target=adder, args=(box2, items))
    tt2 = threading.Thread(target=remover, args=(box2, items))
    tt1.start()
    tt2.start()
    tt1.join()
    tt2.join()
    print("%s items still in the second box" % box2.total_items)
