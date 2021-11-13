import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)s) %(message)s')

def worker():
    logging.debug('worker running')
    return

w1 = threading.Timer(3, worker)
w1.setName('worker1')
w2 = threading.Timer(3, worker)
w2.setName('worker2')


logging.debug('Start')
w1.start()
w2.start()

logging.debug('waiting before cancelling %s', w2.getName())
time.sleep(2)
logging.debug('cancelling %s', w2.getName())
w2.cancel()
logging.debug('End')