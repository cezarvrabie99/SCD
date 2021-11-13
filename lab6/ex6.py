from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("========= process rank=%s" % rank)

if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print("[%s] sending data %s to process %s" % (rank, data_send, destination_process))
    print("[%s] data received is = %s" % (rank, data_received))

if rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1

    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print("[%s] sending data %s to process %s" % (rank, data_send, destination_process))
    print("[%s] data received is = %s" % (rank, data_received))