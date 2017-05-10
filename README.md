
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

## Run the code:
(If there is instructions in front of the codes, then please run the codes accordingly. Otherwise please follow this instruction below.)

**The code should be run in pyspark on hadoop:**  
spark-submit CODE_NAME.py /user/YOUR_NETIT/NYPD_Complaint_Data_Historic.csv  
hadoop fs -getmerge CODE_NAME.out CODE_NAME.out

**Exception for Column 6-23:**  
In order to run data summary files(e.g. column7_data_summary.py), please do following:     

FIRST RUN:  
spark-submit COLUMN_NUMBER_data_quality.py (eg.column7_data_quality.py) /user/YOUR_NETIT/NYPD_Complaint_Data_Historic.csv  
hadoop fs -getmerge COLUMN_NUMBER_data_quality.out COLUMN_NUMBER_data_quality.out

THEN RUN IN THE FOLDER WHERE YOU SAVED THE OUTPUT IN FIRST STEP:  
spark-submit COLUMN_NUMBER_data_summary.py (eg.column7_data_summary.py) COLUMN_NUMBER_data_quality.out  
hadoop fs -getmerge COLUMN_NUMBER_data_summary.out COLUMN_NUMBER_data_summary.out

## ipython report:

The report uses hadoop results saved on authors' local machines. If you want to reproduce the same analysis, please save your hadoop folder on your local machine and run the ipython notebook in the same folder.   

To do this, you may use to download **one particular output:**  
scp YOUR_NETID@dumbo.es.its.nyu.edu:/home/YOUR_NETID/YOUR_FOLDER/CODE_NAME.out .  

or download **the whole folder:**  
scp -r YOUR_NEDID@dumbo.es.its.nyu.edu:/home/YOUR_NEDID/YOUR_FOLDER .

## Hypotheses analysis:
(reference and data source is in /part 2/reference and data source.txt)

/part 2/location/geojson.ipynb gives the codes to generate corresponding zipcodes for our original data and merge back to our data. /part 2/location/Map.ipynb plots the map for crime, collision and price data based on zipcodes.

/part 2/location/Crime Collision zipcode/combine.ipynb combine the crime frequency and collision frequency data on zipcode and plot the relationship between crime frequency and collision frequency. The zipcode for each unique (Latitude, Longitude) pair is summarized in combine.csv.

/part 2/location/Crime price zipcode/zipcode and price.csv gives the crime frequency and average price joined by zipcode.

We use /part 2/time/Cirme Collision time/NYPD_Motor_Vehicle_Collisions.py to generate weekly grouped collision data, and /part 2/time/col5_compared_to_zipcode.py to generate monthly groupd crime data. /part 2/time/Cirme Collision time/Collision vs crime.ipynb gives the comparison between crime data and collision data trends through time.

/part 2/time/Crime unemployment time/compare to unempolyment.ipynb gives the comparison between unemployment data and crime data trends through time.

```python

```
