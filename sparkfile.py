#-------------------------sparkfile.py----------------------------
from pyspark import SparkContext
from pyspark import SparkFiles
finddistance = "/home/ubuntu/cloudclass/shakespeare.txt"
finddistancename = "shakespeare.txt"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
print "Absolute Path -> %s" % SparkFiles.get(finddistancename)
#-------------------------------------sparkfile.py---------------
