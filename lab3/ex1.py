from io import FileIO
from array import array
import threading


class ScrieText(threading.Thread):
    def __init__(self, texte: array, output: FileIO):
        threading.Thread.__init__(self)
        self.texte = texte
        self.output = output

    def run(self):
        while self.texte:
            text = self.texte.pop()
            sir = ""
            for i in range(10000):
                sir = str(i) + " " + str(text) + "\n"
                self.output.write(sir)
            print('write %s done by %s' % (text, self.name))


def main():
    texte1 = ['text1', 'text2']
    texte2 = ['text3', 'text4']
    texte3 = ['text5', 'text6']
    texte4 = ['text7', 'text8']

    f = open('output_ex1.1.txt', 'w+')
    t1 = ScrieText(texte1, f)
    t2 = ScrieText(texte2, f)
    t3 = ScrieText(texte3, f)
    t4 = ScrieText(texte4, f)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    f.close()


if __name__ == '__main__':
    main()

