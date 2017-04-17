from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

# CMPLNT_NUM 
# TO CHECK IF CMPLNT_NUM is integer and unique 

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
  
def check(x):
 try: 
  int(x)
  return "VALID"
 except:
  if x == "":
   return "NULL"
  else:
   return "INVALID"   
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: (check(x[0]),1)) 
 line = line.reduceByKey(lambda x,y: x+y)
 line =line.map(lambda x: '%s\t%s' %(x[0],x[1]))

 line.saveAsTextFile("column0_data_summary_v2.out") 

 sc.stop()




