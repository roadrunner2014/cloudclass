#------------ streaming app ---------------
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]","NetworkWordCount")
