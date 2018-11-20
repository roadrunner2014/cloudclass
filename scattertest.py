#-------------- scattertest.py --------------------------
# for correct performance, run unbuffered with 3 processes:
# mpiexec -n 3 python26 scratch.py -u
import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    x = numpy.linspace(0,100,11)
else:
    x = None

if rank == 2:
    xlocal = numpy.zeros(9)
else:
    xlocal = numpy.zeros(1)

if rank ==0:
    print "Scatter"

counts = [1,1,9]
comm.Scatterv([x,counts,(0,1,2),MPI.DOUBLE],xlocal)
print ("process " + str(rank) + " has " +str(xlocal))

comm.Barrier()
if rank == 0:
    print "Gather"
    xGathered = numpy.zeros(11)
else:
    xGathered = None

comm.Gatherv(xlocal,[xGathered,counts,(0,1,2),MPI.DOUBLE])
print ("process " + str(rank) + " has " +str(xGathered))

#comm.Reduce(xlocal,x, op = MPI.SUM)
#print x[0]