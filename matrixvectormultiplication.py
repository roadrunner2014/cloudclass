#-------------- matrixvectormultiplcation.py --------------------------
# for correct performance, run unbuffered with 3 processes:
# mpiexec -n 3 python26 matrixvectormultiplcation.py
import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

matrix = numpy.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
vector = numpy.array([1.,2.,3.])

def multiply(v, G):
    result = []
    for i in range(len(G[0])): #this loops through columns of the matrix
        total = 0
        for j in range(len(v)): #this loops through vector coordinates & rows of matrix
            total += v[j] * G[j][i]
        result.append(total)
    return result

# Set local empty matrix and vector for use in processes
local_matrix = numpy.empty([3.,3.])
local_vector = numpy.empty([3.])

# Send matrix to processes using Scatter
comm.Scatter(matrix,local_matrix)

# Send vector to processes using Scatter
comm.Scatter(vector,local_vector)

#local computation of dot product
local_product = local_matrix * local_vector
print ("Process " + str(rank) + "Local calculation =", local_product)


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