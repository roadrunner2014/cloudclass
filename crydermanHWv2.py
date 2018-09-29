# Jay Cryderman #01308559
# HW #2
# import math package to allow for more function arguments
from math import *
import sys
# Here the parameters for numerical integration are defined
N = int(input("Enter how many times you want to sum (more times = more accurate): "))
a = float(input("Enter the lower integration bound: "))
b = float(input("Enter the upper integration bound: "))


# Hand calculation for 3x^2 function
def fx(z):
    return 3*z**2

#handCalc = ((b - a)*((fx(a) + fx(b))/2))

handCalc12 = ((2 - 1)*((fx(1) + fx(2))/2))
handCalc23 = ((3 - 2)*((fx(2) + fx(3))/2))
handCalc34 = ((4 - 3)*((fx(3) + fx(4))/2))
handCalc45 = ((5 - 4)*((fx(4) + fx(5))/2))
handCalc = handCalc12 + handCalc23 + handCalc34 + handCalc45


# This is the integration function which performs the integration
def Integrate(nn, aa, bb):
    def f(x):
        # type your function after return
        return 3*x**2

    h = float((b - a) / nn)
    value=0
    value2=0
    for n in range(1,nn):
        value += f(aa + (n -1)*h)
        #value += (f(aa + (n - 2)*h) + f(a + (n - 1)*h))
        value2 = ((bb - aa)/(2*nn))*(fx(aa) + 2*value + fx(bb))
    return value2


# Calculating true error
def trueerror(hcc,fun):
    te = abs((hcc - fun)/hcc)*100
    return te

#def findpolygons(nnn, aaa, bbb):
#    if trueerror(handCalc,Integrate(nnn,aaa,bbb)) > 1E05:
#        nnn += 100 + nnn


functionestimate = Integrate(N,a,b)
h = float((b - a) / N)

def findpolygons(nnn,aaa,bbb):
    finderror = trueerror(handCalc,Integrate(nnn,aaa,bbb))
    while finderror > 1E-5:
        nnn += nnn + 100
        finderror = trueerror(handCalc,Integrate(nnn,aaa,bbb))
    return nnn


def findpolys(xxx):
    if  xxx < 1E-5:
        print "Good job, polygons = ", N
    else:
        print "keep trying"
    return



# Outputs including the integration value:
print(".....................")
print("Hand calculation: "), handCalc
print("h = "), h
polys = findpolygons(N, a, b)
funest = Integrate(polys, a, b)
print(" Here is the area under curve = "), funest
print("number of rounds to get error = "), polys
print("Error = "), trueerror(handCalc,funest)

