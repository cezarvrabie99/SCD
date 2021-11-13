import mpi4py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("========= process rank=%s" % rank)

if rank == 0:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("[%s] sending data %s to process %s" % (rank, data, destination_process))

if rank == 1:
    data = "hello"
    destination_process = 8
    comm.send(data, dest=destination_process)
    print("[%s] sending data %s to process %s" % (rank, data, destination_process))

if rank == 4:
    data = comm.recv(source=0)
    print("[%s] data received is = %s" % (rank, data))

if rank == 8:
    data = comm.recv(source=1)
    print("[%s] data received is = %s" % (rank, data))
