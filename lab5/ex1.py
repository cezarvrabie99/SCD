import multiprocessing
import time
import os


def afiseaza(id):
    print('procesul creat este ', id, ' | pid = ', os.getpid())
    time.sleep(5)
    return


if __name__ == '__main__':
    print("START ... pid = ", os.getpid())
    for id in range(5):
        p = multiprocessing.Process(target=afiseaza, args=(id,))
        p.start()
        p.join()
