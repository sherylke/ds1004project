#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

columns = data.map(lambda x: (x[19],x[20])).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)

sort = columns.sortByKey()

sort.saveAsTextFile('column19_20_quality_issue.out')

sc.stop()

