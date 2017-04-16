#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

code = data.map(lambda x: x[15])

def condition(x):
        if x == '' or x.lower() == 'nan' or x == ' ':
                return ('NaN', 'NULL')
        elif x in ['INSIDE', 'OUTSIDE', 'FRONT OF', 'OPPOSITE OF', 'REAR OF']:
                return (x, 'VALID')
        else:
                return (x, 'INVALID')

output = code.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'TEXT', 'occurrence location', condition(x)[1]))
output.saveAsTextFile("loc_of_occur_desc.out")

sc.stop()
