# sample program 2

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	data = [123, 233, 543, 656, 456, 234, 675, 654, 546]
	for i in range(10):
		comm.send(data[i], dest=i+1, tag=21)
else:
	data = comm.recv(source=0, tag=21)
	print "I am %d, and I got %3.0f.\n" %(rank,data)

