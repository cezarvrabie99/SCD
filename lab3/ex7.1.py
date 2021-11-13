import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)s) %(message)s')


def worker1(e: threading.Event):
    logging.debug('Asteapta evenimentul pentru a continua procesarea...')
    e.wait()
    time.sleep(3)
    logging.debug('Se continua procesarea')


def worker2(e: threading.Event):
    time.sleep(3)
    logging.debug('Se creeaza evenimentul...')
    e.set()
    time.sleep(3)
    logging.debug('Evenimentul a fost creat')


e = threading.Event()

w1 = threading.Thread(name='worker1', target=worker1, args=(e,))
w2 = threading.Thread(name='worker2', target=worker2, args=(e,))

w1.start()
w2.start()
