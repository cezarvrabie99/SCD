import threading
import time

def afiseaza1():
  print("start " + threading.currentThread().getName() + "\n")
  time.sleep(2)
  print("end " + threading.currentThread().getName() + "\n")
  return


def afiseaza2():
  print("start " + threading.currentThread().getName() + "\n")
  time.sleep(2)
  print("end " + threading.currentThread().getName() + "\n")
  return


def afiseaza3():
  print("start " + threading.currentThread().getName() + "\n")
  time.sleep(2)
  print("end " + threading.currentThread().getName() + "\n")
  return


if __name__ == "__main__":
  t1 = threading.Thread(name="a1", target=afiseaza1)
  t2 = threading.Thread(name="a2", target=afiseaza2)
  t3 = threading.Thread(name="a3", target=afiseaza3)

  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()
