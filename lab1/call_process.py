import os

print("Start process")
print("pid = " + str(os.getpid()))

print("Introduceti comenzi")
print("Pentru oprire tastati exit")

while True:
    cmd = input("Comanda: ")
    os.system(cmd)
    if cmd == "exit":
        break

print("End call process")
