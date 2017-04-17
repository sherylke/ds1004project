#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

code = data.map(lambda x: x[14])

precinct = [1,5,6,7,9,10,13,14,17,18,19,20,22,23,24,25,26,28,30,32,33,34,40,41,42,43,44,45,46,47,48,49,50,52,60,61,62,63,66,67,68,69,70,71,72,73,75,76,77,78,79,81,83,84,88,90,94,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123]
# http://www.nyc.gov/html/nypd/html/home/precincts.shtml

def condition(x):
        try:
                if x == '' or x.lower() == 'nan' or x == ' ':
                        return ('NaN', 'NULL')
                elif int(x) in precinct:
                        return (x, 'VALID')
                else:
                        return (x, 'INVALID')
        except ValueError:
                return (x, 'INVALID')

output = code.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'INT', 'precinct code', condition(x)[1]))
output.saveAsTextFile("column14_data_quality.out")

sc.stop()

