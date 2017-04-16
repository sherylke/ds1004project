#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

data = csvfile.map(lambda x: x.split("\t"))

output = data.filter(lambda x: x[-1] == u'INVALID').map(lambda x: (x[0].encode('utf-8'),1)).reduceByKey(lambda x,y: x+y)
output.saveAsTextFile("change_ha.out")

sc.stop()
