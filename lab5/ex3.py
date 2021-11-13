import multiprocessing
import time


def afiseaza():
    print('Start afiseaza')
    time.sleep(0.1)
    print('End afiseaza')


if __name__ ==  '__main__':
    p = multiprocessing.Process(target=afiseaza)
    print('Process before execution: ', p, p.is_alive())
    p.start()
    print('Process running: ', p, p.is_alive())
    p.terminate()
    print('Process terminated: ', p, p.is_alive())
    p.join()
    print('Process joined: ', p, p.is_alive())
    print('Process exit code: ', p.exitcode)


