from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# CMPLNT_FR_DT 
# THIS CODE IS USED TO CHECK DATA QUALITY

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
  
def val_date(fr_dt,fr_tm,to_dt,to_tm,report_dt): 
# first try to make sure the date is a legal date, missing value, or illegal date
 try:
  datetime.datetime.strptime(fr_dt,'%m/%d/%Y')
  return 'VALID'
# second try to make sure the from_datetime is at least earlier than to_datetime
  try:
   to_dttm = datetime.datetime.strptime(to_dt+"/"+to_tm,'%m/%d/%Y/%H:%M:%S')
   fr_dttm = datetime.datetime.strptime(fr_dt+"/"+fr_tm,'%m/%d/%Y/%H:%M:%S')
   report_dt = datetime.datetime.strptime(report_dt,'%m/%d/%Y')  
   if fr_dttm > to_dttm:
    return "INVALID" # if from datetime is greater than to.. it is invalid
   elif fr_dttm > report_dt:
    return "INVALID" # if people report before it happens. it is invalid 
   else:
    return "VALID"
  except:
   return "VALID" 
 except: # if any 2 - 5 col is missing, the first col is still valid
  if fr_dt =='':
   return 'NULL'
  else:
   return 'INVALID'
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: '%s\tDATE\tCompliant from date\t%s' %(x[1],val_date(x[1],x[2],x[3],x[4],x[5])))
 line.saveAsTextFile("column1_data_quality.out") 

 sc.stop()
 
 

