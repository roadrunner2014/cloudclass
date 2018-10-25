import numpy
from mpi4py import MPI
a = numpy([1,2,3])
if MPI.COMM_WORLD.rank == 0:
	MPI.COMM_WORLD.Send(a,dest = 1)
else:
	MPI.COMM_WORLD.Recv(a,source = 0)

