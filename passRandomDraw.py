#!/usr/bin/env python
# coding: utf-8

# passRandomDraw.py
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# In[27]:
randNum = numpy.zeros(1)


# In[30]:
if rank == 1:
    randNum = numpy.random.random_sample(1)
    print "Process", rank, "drew the number", randNum[0]
    comm.Send(randNum, dest=0)

# In[31]:
if rank == 0:
    print "Process", rank, "before receiving has the number", randNum[0]
    comm.Recv(randNum, source=1)
    print "Process", rank, "drew the number", randNum[0]
