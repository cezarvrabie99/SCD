import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)s) %(message)s')

def worker1(e: threading.Event):
    #asteapta sa se produca evenimentul
    logging.debug('asteapta eveniemtnul')
    eveniment = e.wait()
    logging.debug('Se continua procesarea ... ')

e = threading.Event()
e2 = threading.Event()
e3 = threading.Event()

w1 = threading.Thread(name='worker1', target=worker1, args=(e,))
w2 = threading.Thread(name='worker1', target=worker1, args=(e2,))
w3 = threading.Thread(name='worker1', target=worker1, args=(e3,))

w1.start()
w2.start()
w3.start()

logging.debug('Evenimentul 1 va fi generat ...')
time.sleep(3)
e.set()
logging.debug('Evenimentul 1 a fost generat')

logging.debug('Evenimentul 2 va fi generat ...')
time.sleep(3)
e2.set()
logging.debug('Evenimentul 2 a fost generat')

logging.debug('Evenimentul 3 va fi generat ...')
time.sleep(3)
e3.set()
logging.debug('Evenimentul 3 a fost generat')