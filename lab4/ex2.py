from threading import Thread
import sys
from timeit import Timer


class threads_object(Thread):
    def run(self):
        function_to_run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


class nothreads_object(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()


def function_to_run():
    fh = open("README.md", "rb")
    size = 1024
    for i in range(1000):
        fh.read(size)


def show_results(func_name, results):
    print("%s %f seconds" % (func_name, results))


if __name__ == "__main__":
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print('Start...')
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threaded (%s iters)" % i, best_result)
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)
    print('End...')
