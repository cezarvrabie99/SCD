import multiprocessing
import time
import os


def afiseaza(t):
    procname = multiprocessing.current_process().name
    print('START process ', procname, ' | pid = ', os.getpid())
    time.sleep(t)
    print('END process ', procname, ' | pid = ', os.getpid())


if __name__ == '__main__':
    print("START ... pid = ", os.getpid())

    backgroundProc = multiprocessing.Process(name='background', target=afiseaza, args=(5,))
    backgroundProc.daemon = True

    foregroundProc = multiprocessing.Process(name='foreground', target=afiseaza, args=(5,))
    foregroundProc.daemon = False

    backgroundProc.start()
    foregroundProc.start()
    