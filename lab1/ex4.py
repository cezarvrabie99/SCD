import threading


def afiseaza(i):
  print("Functie apelata de thread-ul %i \n" % i)
  return


for i in range(5):
  t = threading.Thread(target=afiseaza, args=(i,))
  t.start()
  t.join()
