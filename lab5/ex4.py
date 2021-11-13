import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        print('called run metod in process: %s' %self.name)
        time.sleep(1)
        return


if __name__ == '__main__':
    for i in range(5):
        p = MyProcess()
        p.start()
        p.join()