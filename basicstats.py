# ----------- basicstats.py app --------------------
from pyspark import SparkContext
from pyspark.mllib.stat import Statistics
from pyspark.mllib.util import MLUtils

sc = SparkContext("local", "Correlation app")
corrType = "pearson"
Normal = sc.parallelize([56,56,65,65,50,25,87,44,35], 2);
Hypervent = sc.parallelize([87,91,85,91,75, 28, 122, 66,
58,], 2);
corr = Statistics.corr(Normal, Hypervent, corrType)
print 'Correlation: \t%g' % (corr)
