from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# CMPLNT_FR_TM
# THIS CODE IS USED TO CHECK DATA QUALITY

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
  
def val_time(fr_dt,fr_tm,to_dt,to_tm): 
 if fr_tm =="24:00:00":
  fr_tm = "23:59:59" # make a correction for the 24:00:00 back to 23:59:59
 try:
  fr_dttm = datetime.datetime.strptime(fr_dt+"/"+fr_tm,'%m/%d/%Y/%H:%M:%S')
# second try to make sure the from_datetime is at least earlier than to_datetime
  try:
   to_dttm = datetime.datetime.strptime(to_dt+"/"+to_tm,'%m/%d/%Y/%H:%M:%S') 
   if fr_dttm > to_dttm:
    return "INVALID" # if from datetime is greater than to.. it is invalid
   else:
    return "VALID"
  except: # if other columns are missing, I think it is ok 
   return "VALID" 
 except:  
  if fr_tm =='' or fr_dt =='':
   return 'NULL'
  else:
   return 'INVALID'
   
def datetime_func(fr_dt,fr_tm):
 if fr_tm =="24:00:00":
  fr_tm = "23:59:59"
 return datetime.datetime.strptime(fr_dt+"/"+fr_tm,'%m/%d/%Y/%H:%M:%S')
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: [[x[1],x[2]],val_time(x[1],x[2],x[3],x[4])]) # a list of from_time,from_date and if it is valid 
 line = line.filter(lambda x:x[1]=='VALID') 
 line = line.map(lambda x: datetime_func(x[0][0],x[0][1]))
 line = line.map(lambda x: ((x.year,x.isocalendar()[1],x.isocalendar()[2],x.hour),1))
 line = line.reduceByKey(lambda x,y: x+y).sortByKey()
 line = line.map(lambda x: '%s\t%s' %(x[0],x[1])) 
 line.saveAsTextFile("col1and2_hour.out") 

 sc.stop()

