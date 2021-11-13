import mpi4py
from mpi4py import MPI
import os

comm = MPI.COMM_WORLD

print("[%s] hello from process %s" % (os.getpid(), comm.rank))
