#------------------------firstapp.py---------------------------------------
from pyspark import SparkContext
logFile = "file:///home/ubuntu/spark-2.3.2-bin-hadoop2.7/README.md"   
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
#-----------------------------------firstapp.py---------------------------
