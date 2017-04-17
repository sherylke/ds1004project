
# DS-GA1004   
# Big Data Term Project

### Authors:  
Wenjie Sun (ws854)  
Xinyan Yang (xy975)  
Yaohan Ke (yk1587)  

### Google Docs: 
https://docs.google.com/a/nyu.edu/document/d/1Ucm_P7rkLDR4e1tl-qNADEEZ95wo1cWLxQVGxNa_RwQ/edit?usp=sharing

## Please upload the data to your hadoop first: 

**1. Download data:**  
https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i

**2. Upload the data to dumbo:**  
cd "where you saved the data"  
scp NYPD_Complaint_Data_Historic.csv YOUR_NETID@dumbo.es.its.nyu.edu:/home/YOUR_NETID

**3. Put the data into hadoop:**  
hadoop fs -copyFromLocal NYPD_Complaint_Data_Historic.csv 

## Run the hadoop code:

**The code should be run in pyspark on hadoop:**  
spark-submit CODE_NAME.py /user/YOUR_NETIT/NYPD_Complaint_Data_Historic.csv  
hadoop fs -getmerge CODE_NAME.out CODE_NAME.out

## ipython report:

The report uses hadoop results saved on authors' local machines. If you want to reproduce the same analysis, please save your hadoop folder on your local machine and run the ipython notebook in the same folder.   

To do this, you may use to download **one particular output:**  
scp YOUR_NETID@dumbo.es.its.nyu.edu:/home/YOUR_NETID/YOUR_FOLDER/CODE_NAME.out .  

or download **the whole folder:**  
scp -r YOUR_NEDID@dumbo.es.its.nyu.edu:/home/YOUR_NEDID/YOUR_FOLDER .


```python

```
