import time
from array import array
from threading import Thread, Event
import random

items = []
event = Event()


class Consumer(Thread):
    def __init__(self, items: array, event: Event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('\nConsumer: %d extracted from list by %s' % (item, self.name))
            print('--------- items[]=', self.items,'\n\n')


class Producer(Thread):
    def __init__(self, items: array, event: Event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        for i in range(20):
            print('\n========================== ', i, '\n')
            time.sleep(2)

            item = random.randint(0, 256)
            self.items.append(item)
            print('Producer: %d appended to list by %s' % (item, self.name))
            print('Producer: event set by %s' % self.name)
            print('+++++++++++++++ items[]=', self.items)
            self.event.set()
            self.event.clear()


if __name__ == '__main__':
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

