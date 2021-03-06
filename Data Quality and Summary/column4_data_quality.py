from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# CMPLNT_TO_TM
# THIS CODE IS USED TO CHECK DATA QUALITY

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
  
def val_time(fr_dt,fr_tm,to_dt,to_tm): 
# first try to make sure the time is a legal time
 try:
  datetime.datetime.strptime(to_tm,'%H:%M:%S')
# second try to make sure the from_datetime is at least earlier than to_datetime
  try:
   to_dttm = datetime.datetime.strptime(to_dt+"/"+to_tm,'%m/%d/%Y/%H:%M:%S')
   fr_dttm = datetime.datetime.strptime(fr_dt+"/"+fr_tm,'%m/%d/%Y/%H:%M:%S') 
   if fr_dttm > to_dttm:
    return "INVALID" # if from datetime is greater than to.. it is invalid
   else:
    return "VALID"
  except: # if other columns are missing, I think it is ok 
   return "VALID" 
 except:  
  if to_tm =='':
   return 'NULL'
  else:
   return 'INVALID'
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: '%s\tTIME\tCompliant to time\t%s' %(x[4],val_time(x[1],x[2],x[3],x[4])))
 line.saveAsTextFile("column4_data_quality.out") 

 sc.stop()