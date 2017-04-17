#!/usr/bin/env python

import sys
from pyspark import SparkContext

sc = SparkContext()

file = sc.textFile(sys.argv[1], 1)

data = file.map(lambda x: x.split("\t"))

output = data.map(lambda x: (x[-1],1)).reduceByKey(lambda x,y: x+y).map(lambda x: '%s\t%s' % (x[0], x[1]))
output.saveAsTextFile('column9_data_summary.out')

sc.stop()
