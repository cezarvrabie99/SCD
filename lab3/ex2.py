from io import FileIO
from array import array
import threading


class ScrieText(threading.Thread):
    def __init__(self, texte: array, output: FileIO, lock: threading.Lock):
        threading.Thread.__init__(self)
        self.texte = texte
        self.output = output
        self.lock = lock

    def run(self):
        while self.texte:
            text = self.texte.pop()
            self.lock.acquire()
            print('lock acquired by %s' % self.name)
            sir = ""
            for i in range(10000):
                sir = str(i) + " " + str(text) + "\n"
                self.output.write(sir)
            print('write %s done by %s' % (text, self.name))
            print('lock released by %s' % self.name)
            self.lock.release()


def main():
    texte1 = ['text1', 'text2']
    texte2 = ['text3', 'text4']

    f = open('output_ex2.txt', 'w+')
    lock = threading.Lock()

    t1 = ScrieText(texte1, f, lock)
    t2 = ScrieText(texte2, f, lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    f.close()


if __name__ == '__main__':
    main()

