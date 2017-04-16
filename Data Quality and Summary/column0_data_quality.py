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
 
  
def check(x0,x1):
 try:
  int(x0)
  if x1[1]==1:
   return "VALID"
  else:
   return "INVALID" # if the count of the key is more than one. it is not unique.. 
 except:
  if x0=="":
   return "NULL"
  else:
   return "INVALID"   
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 count = line.map(lambda x:(x[0],1)).reduceByKey(lambda x,y:x+y)
 cmplnt_num = line.map(lambda x:(x[0],0)) 
 cmplnt = cmplnt_num.leftOuterJoin(count)
 cmplnt = cmplnt.map(lambda x: "%s\tINTEGER\tA unique compliant number\t%s" %(x[0],check(x[0],x[1])))
 
 
 cmplnt.saveAsTextFile("column0_data_quality.out") 

 sc.stop()




