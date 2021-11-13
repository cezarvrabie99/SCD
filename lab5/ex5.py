import multiprocessing
import time
import random
import os


class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('[producer %d]: item %d appended by %s' % (os.getpid(), item, self.name))
            time.sleep(1)
            print('[producer] queue size =%s' % self.queue.qsize())


class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            time.sleep(3)
            item = self.queue.get()
            print('[consumer %d]: item %d extracted by %s' % (os.getpid(), item, self.name))
            print('[producer] queue size =%s' % self.queue.qsize())
            if self.queue.qsize() == 0:
                break


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_producer.join()
