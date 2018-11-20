#dotProductParallel_1.py
#"to run" syntax example: mpiexec -n 4 python dotProductParallel_1.py 40000

from mpi4py import MPI
import numpy
import sys
import time

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#read from command line
n = int(sys.argv[1]) #length of vectors

#arbitrary example vectors, generated to be evenly divided by the
#number of processes for convenience
# send data vectors
x = numpy.linspace(0,100,size*n) if comm.rank == 0 else None
y = numpy.linspace(20,300,size*n) if comm.rank == 0 else None

# Calculation of counts and displacements for Scatterv
counts = numpy.empty([size], dtype=int)
dspls = numpy.empty([size], dtype=int)
countstep = n / size
countstepextra = n % size
finalcountstep = countstep + countstepextra
sum = 0            #Sum of counts. Used to calculate displacements

for i in range(0,size,1):
    counts[i] = countstep
    dspls[i] = sum
    sum += 1


#initialize as numpy arrays
dot = numpy.array([0.])
local_n = numpy.array([0], dtype=int)

#length of each process's portion of the original vector
local_n = numpy.array([n/size], dtype=int)

#communicate local array size to all processes
comm.Bcast(local_n, root=0)

#initialize as numpy arrays for receive data
local_x = numpy.zeros(local_n)
local_y = numpy.zeros(local_n)

#divide up vectors
# example of comm.Scatterv(sendbuf, recvbuf, int root=0) where sendbuf = [data, counts, displacements, type]
comm.Scatterv([x,counts,dspls,MPI.DOUBLE],local_x,root=0)
comm.Scatterv([y,counts,dspls,MPI.DOUBLE],local_y,root=0)


#local computation of dot product
local_dot = numpy.array([numpy.dot(local_x, local_y)])
print ("Process " + str(rank) + "Local dot calculation =", local_dot)

#comm.Barrier()
#sum the results of each
sendbuf = [local_dot,counts[rank]]
recvbuf = [dot,counts,dspls, MPI.DOUBLE]
comm.Gatherv(sendbuf,recvbuf,root=0)
print ("Process " + str(rank) + " Gather dot calculation =", dot)

#sum the results of each
comm.Reduce(local_dot, dot, op = MPI.SUM)

#comm.Reduce(local_dot, dot, op = MPI.MAX(local_dot,dot))
if (rank == 0):
    print "The dot product is", dot[0], "computed in parallel"
    print "and", numpy.dot(x,y), "computed serially"

end = time.time()
print "Time to compute = ", (end-start)