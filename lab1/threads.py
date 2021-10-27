from threading import Thread
from time import sleep

class MyThread(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.mesaj = "init fir \n"

  def afisare(self):
    print(self.mesaj)

  def run(self):
    print("start thread")
    x = 0
    while (x<10):
      self.afisare()
      sleep(2)
      x += 1
    print("end thread")

print("Start process")
thd = MyThread()
thd.start()
print("End process")
