

```python
import pandas as pd
data = pd.read_csv('./NYPD_Complaint_Data_Historic.csv')
```

    //anaconda/lib/python3.5/site-packages/IPython/core/interactiveshell.py:2717: DtypeWarning: Columns (17) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)



```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CMPLNT_NUM</th>
      <th>CMPLNT_FR_DT</th>
      <th>CMPLNT_FR_TM</th>
      <th>CMPLNT_TO_DT</th>
      <th>CMPLNT_TO_TM</th>
      <th>RPT_DT</th>
      <th>KY_CD</th>
      <th>OFNS_DESC</th>
      <th>PD_CD</th>
      <th>PD_DESC</th>
      <th>...</th>
      <th>ADDR_PCT_CD</th>
      <th>LOC_OF_OCCUR_DESC</th>
      <th>PREM_TYP_DESC</th>
      <th>PARKS_NM</th>
      <th>HADEVELOPT</th>
      <th>X_COORD_CD</th>
      <th>Y_COORD_CD</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Lat_Lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101109527</td>
      <td>12/31/2015</td>
      <td>23:45:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12/31/2015</td>
      <td>113</td>
      <td>FORGERY</td>
      <td>729.0</td>
      <td>FORGERY,ETC.,UNCLASSIFIED-FELO</td>
      <td>...</td>
      <td>44.0</td>
      <td>INSIDE</td>
      <td>BAR/NIGHT CLUB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1007314.0</td>
      <td>241257.0</td>
      <td>40.828848</td>
      <td>-73.916661</td>
      <td>(40.828848333, -73.916661142)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>153401121</td>
      <td>12/31/2015</td>
      <td>23:36:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12/31/2015</td>
      <td>101</td>
      <td>MURDER &amp; NON-NEGL. MANSLAUGHTER</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>103.0</td>
      <td>OUTSIDE</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1043991.0</td>
      <td>193406.0</td>
      <td>40.697338</td>
      <td>-73.784557</td>
      <td>(40.697338138, -73.784556739)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>569369778</td>
      <td>12/31/2015</td>
      <td>23:30:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12/31/2015</td>
      <td>117</td>
      <td>DANGEROUS DRUGS</td>
      <td>503.0</td>
      <td>CONTROLLED SUBSTANCE,INTENT TO</td>
      <td>...</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>OTHER</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>999463.0</td>
      <td>231690.0</td>
      <td>40.802607</td>
      <td>-73.945052</td>
      <td>(40.802606608, -73.945051911)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>968417082</td>
      <td>12/31/2015</td>
      <td>23:30:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12/31/2015</td>
      <td>344</td>
      <td>ASSAULT 3 &amp; RELATED OFFENSES</td>
      <td>101.0</td>
      <td>ASSAULT 3</td>
      <td>...</td>
      <td>105.0</td>
      <td>INSIDE</td>
      <td>RESIDENCE-HOUSE</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1060183.0</td>
      <td>177862.0</td>
      <td>40.654549</td>
      <td>-73.726339</td>
      <td>(40.654549444, -73.726338791)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>641637920</td>
      <td>12/31/2015</td>
      <td>23:25:00</td>
      <td>12/31/2015</td>
      <td>23:30:00</td>
      <td>12/31/2015</td>
      <td>344</td>
      <td>ASSAULT 3 &amp; RELATED OFFENSES</td>
      <td>101.0</td>
      <td>ASSAULT 3</td>
      <td>...</td>
      <td>13.0</td>
      <td>FRONT OF</td>
      <td>OTHER</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>987606.0</td>
      <td>208148.0</td>
      <td>40.738002</td>
      <td>-73.987891</td>
      <td>(40.7380024, -73.98789129)</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>




```python
precinct = [1,5,6,7,9,10,13,14,17,18,19,20,22,23,24,25,26,28,30,32,33,34,40,41,42,43,44,45,46,47,48,49,50,52,60,61,62,63,66,67,68,69,70,71,72,73,75,76,77,78,79,81,83,84,88,90,94,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123]
```


```python
"what" == 'what'
```




    True




```python
["O'Dwyer Gardens", 'what'][0].upper()
```




    "O'DWYER GARDENS"




```python
try:
    print(int('x'))
except ValueError:
    print('INVALID')
```

    INVALID



```python
df = {}
for code in data['KY_CD'].unique():
    df['KY_CD'] = code
    df['OFNS_DESC'] = data[data['KY_CD'] == code]['OFNS_DESC']
```


```python
data[data['KY_CD'] == data['KY_CD'].unique()[2]]['OFNS_DESC'].unique()
```




    array(['DANGEROUS DRUGS', nan], dtype=object)




```python
isinstance('5',int)
```




    False




```python
len(data[data['ADDR_PCT_CD'].isnull()==True])
```




    390




```python

for i in len(data):
    if 
    data['CMPLNT_TO_DT']
    len(data[data['CMPLNT_TO_DT'].isnull()==True])
```




    nan




```python
data['CMPLNT_FR_DT'][data['CMPLNT_FR_DT'].isnull()==True].count()
```




    0




```python
data['CMPLNT_FR_TM'][data['CMPLNT_FR_TM'].isnull()==True].count()
```




    0




```python
data['CMPLNT_TO_DT'][data['CMPLNT_TO_DT'].isna()==True].count()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-6f1c5e8ae3b6> in <module>()
    ----> 1 data['CMPLNT_TO_DT'][data['CMPLNT_TO_DT'].isna()==True].count()
    

    //anaconda/lib/python3.5/site-packages/pandas/core/generic.py in __getattr__(self, name)
       2742             if name in self._info_axis:
       2743                 return self[name]
    -> 2744             return object.__getattribute__(self, name)
       2745 
       2746     def __setattr__(self, name, value):


    AttributeError: 'Series' object has no attribute 'isna'



```python
data.iloc[-1,:]
```




    CMPLNT_NUM                                                   673950804
    CMPLNT_FR_DT                                                       NaN
    CMPLNT_FR_TM                                                  22:00:00
    CMPLNT_TO_DT                                                01/01/2006
    CMPLNT_TO_TM                                                  13:00:00
    RPT_DT                                                      01/01/2006
    KY_CD                                                              109
    OFNS_DESC                                                GRAND LARCENY
    PD_CD                                                              457
    PD_DESC              LARCENY,GRAND OF VEHICULAR/MOTORCYCLE ACCESSORIES
    CRM_ATPT_CPTD_CD                                             COMPLETED
    LAW_CAT_CD                                                      FELONY
    JURIS_DESC                                            N.Y. POLICE DEPT
    BORO_NM                                                       BROOKLYN
    ADDR_PCT_CD                                                         61
    LOC_OF_OCCUR_DESC                                             FRONT OF
    PREM_TYP_DESC                                                   STREET
    PARKS_NM                                                           NaN
    HADEVELOPT                                                         NaN
    X_COORD_CD                                                      999199
    Y_COORD_CD                                                      163370
    Latitude                                                       40.6151
    Longitude                                                     -73.9462
    Lat_Lon                                  (40.615084921, -73.946157157)
    Name: 5101230, dtype: object




```python
'1\t2\t3\t4'.split('\t')[-1]
```




    '4'




```python
u'NAN'
```




    'NAN'




```python
import numpy as np
```


```python
names = np.fromstring('parks_nm.txt')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-15-7a67e7790ed3> in <module>()
    ----> 1 names = np.fromstring('parks_nm.txt')
    

    ValueError: string size must be a multiple of element size



```python
names = np.genfromtxt('parks_nm.txt',dtype='str')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-18-d49e61ceb9cb> in <module>()
    ----> 1 names = np.genfromtxt('parks_nm.txt',dtype='str')
    

    //anaconda/lib/python3.5/site-packages/numpy/lib/npyio.py in genfromtxt(fname, dtype, comments, delimiter, skip_header, skip_footer, converters, missing_values, filling_values, usecols, names, excludelist, deletechars, replace_space, autostrip, case_sensitive, defaultfmt, unpack, usemask, loose, invalid_raise, max_rows)
       1826             # Raise an exception ?
       1827             if invalid_raise:
    -> 1828                 raise ValueError(errmsg)
       1829             # Issue a warning ?
       1830             else:


    ValueError: Some errors were detected !
        Line #2 (got 3 columns instead of 2)
        Line #3 (got 3 columns instead of 2)
        Line #12 (got 3 columns instead of 2)
        Line #18 (got 3 columns instead of 2)
        Line #20 (got 3 columns instead of 2)
        Line #22 (got 4 columns instead of 2)
        Line #23 (got 3 columns instead of 2)
        Line #29 (got 3 columns instead of 2)
        Line #37 (got 3 columns instead of 2)
        Line #39 (got 5 columns instead of 2)
        Line #40 (got 3 columns instead of 2)
        Line #41 (got 3 columns instead of 2)
        Line #44 (got 5 columns instead of 2)
        Line #47 (got 3 columns instead of 2)
        Line #51 (got 3 columns instead of 2)
        Line #54 (got 3 columns instead of 2)
        Line #55 (got 3 columns instead of 2)
        Line #56 (got 3 columns instead of 2)
        Line #59 (got 3 columns instead of 2)
        Line #62 (got 3 columns instead of 2)
        Line #65 (got 3 columns instead of 2)
        Line #67 (got 3 columns instead of 2)
        Line #69 (got 4 columns instead of 2)
        Line #73 (got 3 columns instead of 2)
        Line #77 (got 1 columns instead of 2)
        Line #78 (got 4 columns instead of 2)
        Line #79 (got 3 columns instead of 2)
        Line #80 (got 4 columns instead of 2)
        Line #83 (got 3 columns instead of 2)
        Line #84 (got 3 columns instead of 2)
        Line #85 (got 4 columns instead of 2)
        Line #88 (got 3 columns instead of 2)
        Line #93 (got 3 columns instead of 2)
        Line #95 (got 3 columns instead of 2)
        Line #100 (got 3 columns instead of 2)
        Line #101 (got 3 columns instead of 2)
        Line #111 (got 3 columns instead of 2)
        Line #112 (got 3 columns instead of 2)
        Line #114 (got 3 columns instead of 2)
        Line #117 (got 4 columns instead of 2)
        Line #118 (got 3 columns instead of 2)
        Line #119 (got 4 columns instead of 2)
        Line #120 (got 3 columns instead of 2)
        Line #122 (got 1 columns instead of 2)
        Line #124 (got 3 columns instead of 2)
        Line #125 (got 3 columns instead of 2)
        Line #127 (got 3 columns instead of 2)
        Line #129 (got 4 columns instead of 2)
        Line #130 (got 3 columns instead of 2)
        Line #131 (got 3 columns instead of 2)
        Line #133 (got 4 columns instead of 2)
        Line #134 (got 3 columns instead of 2)
        Line #135 (got 3 columns instead of 2)
        Line #139 (got 3 columns instead of 2)
        Line #141 (got 3 columns instead of 2)
        Line #143 (got 6 columns instead of 2)
        Line #145 (got 4 columns instead of 2)
        Line #146 (got 4 columns instead of 2)
        Line #147 (got 3 columns instead of 2)
        Line #150 (got 3 columns instead of 2)
        Line #155 (got 3 columns instead of 2)
        Line #158 (got 5 columns instead of 2)
        Line #165 (got 3 columns instead of 2)
        Line #166 (got 3 columns instead of 2)
        Line #167 (got 3 columns instead of 2)
        Line #173 (got 3 columns instead of 2)
        Line #176 (got 3 columns instead of 2)
        Line #177 (got 4 columns instead of 2)
        Line #178 (got 3 columns instead of 2)
        Line #179 (got 3 columns instead of 2)
        Line #181 (got 1 columns instead of 2)
        Line #185 (got 4 columns instead of 2)
        Line #186 (got 3 columns instead of 2)
        Line #189 (got 4 columns instead of 2)
        Line #191 (got 3 columns instead of 2)
        Line #192 (got 5 columns instead of 2)
        Line #198 (got 3 columns instead of 2)
        Line #205 (got 3 columns instead of 2)
        Line #206 (got 4 columns instead of 2)
        Line #207 (got 5 columns instead of 2)
        Line #208 (got 3 columns instead of 2)
        Line #210 (got 3 columns instead of 2)
        Line #211 (got 3 columns instead of 2)
        Line #212 (got 3 columns instead of 2)
        Line #216 (got 3 columns instead of 2)
        Line #217 (got 3 columns instead of 2)
        Line #219 (got 4 columns instead of 2)
        Line #220 (got 3 columns instead of 2)
        Line #221 (got 3 columns instead of 2)
        Line #224 (got 3 columns instead of 2)
        Line #225 (got 3 columns instead of 2)
        Line #231 (got 3 columns instead of 2)
        Line #232 (got 3 columns instead of 2)
        Line #233 (got 3 columns instead of 2)
        Line #234 (got 4 columns instead of 2)
        Line #235 (got 3 columns instead of 2)
        Line #236 (got 3 columns instead of 2)
        Line #237 (got 3 columns instead of 2)
        Line #239 (got 4 columns instead of 2)
        Line #241 (got 4 columns instead of 2)
        Line #244 (got 3 columns instead of 2)
        Line #245 (got 3 columns instead of 2)
        Line #247 (got 3 columns instead of 2)
        Line #249 (got 1 columns instead of 2)
        Line #252 (got 3 columns instead of 2)
        Line #253 (got 3 columns instead of 2)
        Line #254 (got 3 columns instead of 2)
        Line #255 (got 3 columns instead of 2)
        Line #257 (got 3 columns instead of 2)
        Line #265 (got 3 columns instead of 2)
        Line #268 (got 4 columns instead of 2)
        Line #269 (got 3 columns instead of 2)
        Line #270 (got 4 columns instead of 2)
        Line #277 (got 3 columns instead of 2)
        Line #281 (got 4 columns instead of 2)
        Line #282 (got 3 columns instead of 2)
        Line #287 (got 4 columns instead of 2)
        Line #289 (got 4 columns instead of 2)
        Line #294 (got 3 columns instead of 2)
        Line #295 (got 3 columns instead of 2)
        Line #296 (got 3 columns instead of 2)
        Line #298 (got 4 columns instead of 2)
        Line #302 (got 3 columns instead of 2)
        Line #308 (got 3 columns instead of 2)
        Line #311 (got 3 columns instead of 2)
        Line #313 (got 3 columns instead of 2)
        Line #315 (got 3 columns instead of 2)
        Line #320 (got 3 columns instead of 2)
        Line #323 (got 4 columns instead of 2)
        Line #324 (got 3 columns instead of 2)
        Line #325 (got 3 columns instead of 2)
        Line #326 (got 3 columns instead of 2)
        Line #327 (got 3 columns instead of 2)
        Line #329 (got 3 columns instead of 2)
        Line #330 (got 3 columns instead of 2)
        Line #333 (got 3 columns instead of 2)
        Line #335 (got 3 columns instead of 2)
        Line #338 (got 5 columns instead of 2)
        Line #344 (got 3 columns instead of 2)
        Line #348 (got 3 columns instead of 2)
        Line #349 (got 3 columns instead of 2)
        Line #350 (got 4 columns instead of 2)
        Line #352 (got 3 columns instead of 2)
        Line #353 (got 5 columns instead of 2)
        Line #354 (got 4 columns instead of 2)
        Line #355 (got 4 columns instead of 2)
        Line #356 (got 3 columns instead of 2)
        Line #358 (got 3 columns instead of 2)
        Line #360 (got 3 columns instead of 2)
        Line #363 (got 3 columns instead of 2)
        Line #364 (got 3 columns instead of 2)
        Line #367 (got 3 columns instead of 2)
        Line #368 (got 3 columns instead of 2)
        Line #371 (got 4 columns instead of 2)
        Line #372 (got 3 columns instead of 2)
        Line #376 (got 3 columns instead of 2)
        Line #377 (got 4 columns instead of 2)
        Line #379 (got 3 columns instead of 2)
        Line #380 (got 4 columns instead of 2)
        Line #382 (got 3 columns instead of 2)
        Line #384 (got 3 columns instead of 2)
        Line #385 (got 3 columns instead of 2)
        Line #386 (got 3 columns instead of 2)
        Line #391 (got 3 columns instead of 2)
        Line #393 (got 3 columns instead of 2)
        Line #396 (got 3 columns instead of 2)
        Line #400 (got 3 columns instead of 2)
        Line #401 (got 3 columns instead of 2)
        Line #402 (got 4 columns instead of 2)
        Line #403 (got 3 columns instead of 2)
        Line #404 (got 3 columns instead of 2)
        Line #405 (got 3 columns instead of 2)
        Line #409 (got 4 columns instead of 2)
        Line #412 (got 4 columns instead of 2)
        Line #418 (got 4 columns instead of 2)
        Line #419 (got 3 columns instead of 2)
        Line #422 (got 3 columns instead of 2)
        Line #425 (got 3 columns instead of 2)
        Line #426 (got 3 columns instead of 2)
        Line #430 (got 3 columns instead of 2)
        Line #434 (got 3 columns instead of 2)
        Line #437 (got 3 columns instead of 2)
        Line #438 (got 3 columns instead of 2)
        Line #439 (got 3 columns instead of 2)
        Line #440 (got 4 columns instead of 2)
        Line #441 (got 3 columns instead of 2)
        Line #445 (got 4 columns instead of 2)
        Line #446 (got 4 columns instead of 2)
        Line #447 (got 3 columns instead of 2)
        Line #451 (got 3 columns instead of 2)
        Line #454 (got 4 columns instead of 2)
        Line #459 (got 3 columns instead of 2)
        Line #460 (got 5 columns instead of 2)
        Line #461 (got 3 columns instead of 2)
        Line #462 (got 3 columns instead of 2)
        Line #463 (got 3 columns instead of 2)
        Line #464 (got 3 columns instead of 2)
        Line #465 (got 3 columns instead of 2)
        Line #466 (got 3 columns instead of 2)
        Line #468 (got 3 columns instead of 2)
        Line #469 (got 4 columns instead of 2)
        Line #470 (got 3 columns instead of 2)
        Line #471 (got 4 columns instead of 2)
        Line #472 (got 4 columns instead of 2)
        Line #474 (got 3 columns instead of 2)
        Line #476 (got 3 columns instead of 2)
        Line #478 (got 3 columns instead of 2)
        Line #480 (got 4 columns instead of 2)
        Line #482 (got 3 columns instead of 2)
        Line #483 (got 3 columns instead of 2)
        Line #484 (got 3 columns instead of 2)
        Line #486 (got 3 columns instead of 2)
        Line #489 (got 7 columns instead of 2)
        Line #491 (got 3 columns instead of 2)
        Line #495 (got 3 columns instead of 2)
        Line #499 (got 5 columns instead of 2)
        Line #500 (got 4 columns instead of 2)
        Line #504 (got 3 columns instead of 2)
        Line #505 (got 4 columns instead of 2)
        Line #506 (got 3 columns instead of 2)
        Line #507 (got 3 columns instead of 2)
        Line #508 (got 3 columns instead of 2)
        Line #509 (got 3 columns instead of 2)
        Line #511 (got 3 columns instead of 2)
        Line #513 (got 3 columns instead of 2)
        Line #515 (got 5 columns instead of 2)
        Line #516 (got 3 columns instead of 2)
        Line #525 (got 3 columns instead of 2)
        Line #529 (got 3 columns instead of 2)
        Line #530 (got 3 columns instead of 2)
        Line #531 (got 3 columns instead of 2)
        Line #532 (got 3 columns instead of 2)
        Line #533 (got 3 columns instead of 2)
        Line #536 (got 3 columns instead of 2)
        Line #539 (got 3 columns instead of 2)
        Line #540 (got 5 columns instead of 2)
        Line #541 (got 6 columns instead of 2)
        Line #542 (got 3 columns instead of 2)
        Line #544 (got 3 columns instead of 2)
        Line #545 (got 3 columns instead of 2)
        Line #546 (got 3 columns instead of 2)
        Line #549 (got 3 columns instead of 2)
        Line #551 (got 4 columns instead of 2)
        Line #552 (got 3 columns instead of 2)
        Line #553 (got 3 columns instead of 2)
        Line #554 (got 3 columns instead of 2)
        Line #558 (got 1 columns instead of 2)
        Line #559 (got 3 columns instead of 2)
        Line #561 (got 3 columns instead of 2)
        Line #562 (got 3 columns instead of 2)
        Line #564 (got 3 columns instead of 2)
        Line #576 (got 3 columns instead of 2)
        Line #577 (got 7 columns instead of 2)
        Line #581 (got 3 columns instead of 2)
        Line #582 (got 4 columns instead of 2)
        Line #584 (got 4 columns instead of 2)
        Line #585 (got 3 columns instead of 2)
        Line #586 (got 3 columns instead of 2)
        Line #587 (got 3 columns instead of 2)
        Line #588 (got 3 columns instead of 2)
        Line #589 (got 3 columns instead of 2)
        Line #590 (got 3 columns instead of 2)
        Line #591 (got 3 columns instead of 2)
        Line #593 (got 3 columns instead of 2)
        Line #595 (got 3 columns instead of 2)
        Line #596 (got 3 columns instead of 2)
        Line #597 (got 3 columns instead of 2)
        Line #604 (got 5 columns instead of 2)
        Line #605 (got 4 columns instead of 2)
        Line #606 (got 3 columns instead of 2)
        Line #608 (got 4 columns instead of 2)
        Line #610 (got 3 columns instead of 2)
        Line #611 (got 3 columns instead of 2)
        Line #615 (got 3 columns instead of 2)
        Line #616 (got 3 columns instead of 2)
        Line #617 (got 3 columns instead of 2)
        Line #618 (got 3 columns instead of 2)
        Line #619 (got 4 columns instead of 2)
        Line #620 (got 4 columns instead of 2)
        Line #621 (got 3 columns instead of 2)
        Line #622 (got 3 columns instead of 2)
        Line #634 (got 3 columns instead of 2)
        Line #635 (got 3 columns instead of 2)
        Line #637 (got 3 columns instead of 2)
        Line #638 (got 3 columns instead of 2)
        Line #639 (got 4 columns instead of 2)
        Line #643 (got 3 columns instead of 2)
        Line #644 (got 1 columns instead of 2)
        Line #645 (got 3 columns instead of 2)
        Line #654 (got 3 columns instead of 2)
        Line #655 (got 3 columns instead of 2)
        Line #657 (got 3 columns instead of 2)
        Line #658 (got 3 columns instead of 2)
        Line #662 (got 3 columns instead of 2)
        Line #666 (got 3 columns instead of 2)
        Line #671 (got 4 columns instead of 2)
        Line #673 (got 3 columns instead of 2)
        Line #674 (got 3 columns instead of 2)
        Line #676 (got 3 columns instead of 2)
        Line #677 (got 3 columns instead of 2)
        Line #678 (got 5 columns instead of 2)
        Line #680 (got 3 columns instead of 2)
        Line #681 (got 3 columns instead of 2)
        Line #682 (got 4 columns instead of 2)
        Line #683 (got 3 columns instead of 2)
        Line #684 (got 3 columns instead of 2)
        Line #685 (got 4 columns instead of 2)
        Line #686 (got 3 columns instead of 2)
        Line #689 (got 3 columns instead of 2)
        Line #691 (got 4 columns instead of 2)
        Line #693 (got 3 columns instead of 2)
        Line #694 (got 3 columns instead of 2)
        Line #697 (got 4 columns instead of 2)
        Line #698 (got 3 columns instead of 2)
        Line #701 (got 4 columns instead of 2)
        Line #704 (got 3 columns instead of 2)
        Line #706 (got 4 columns instead of 2)
        Line #707 (got 3 columns instead of 2)
        Line #709 (got 3 columns instead of 2)
        Line #713 (got 3 columns instead of 2)
        Line #714 (got 3 columns instead of 2)
        Line #715 (got 3 columns instead of 2)
        Line #717 (got 3 columns instead of 2)
        Line #718 (got 4 columns instead of 2)
        Line #720 (got 3 columns instead of 2)
        Line #722 (got 3 columns instead of 2)
        Line #723 (got 4 columns instead of 2)
        Line #727 (got 3 columns instead of 2)
        Line #728 (got 5 columns instead of 2)
        Line #729 (got 3 columns instead of 2)
        Line #730 (got 4 columns instead of 2)
        Line #731 (got 3 columns instead of 2)
        Line #734 (got 4 columns instead of 2)
        Line #738 (got 3 columns instead of 2)
        Line #739 (got 3 columns instead of 2)
        Line #740 (got 5 columns instead of 2)
        Line #741 (got 5 columns instead of 2)
        Line #742 (got 3 columns instead of 2)
        Line #743 (got 3 columns instead of 2)
        Line #746 (got 3 columns instead of 2)
        Line #747 (got 4 columns instead of 2)
        Line #748 (got 3 columns instead of 2)
        Line #749 (got 3 columns instead of 2)
        Line #750 (got 3 columns instead of 2)
        Line #751 (got 3 columns instead of 2)
        Line #752 (got 3 columns instead of 2)
        Line #753 (got 3 columns instead of 2)
        Line #754 (got 3 columns instead of 2)
        Line #755 (got 4 columns instead of 2)
        Line #757 (got 3 columns instead of 2)
        Line #758 (got 3 columns instead of 2)
        Line #759 (got 3 columns instead of 2)
        Line #760 (got 3 columns instead of 2)
        Line #761 (got 3 columns instead of 2)
        Line #762 (got 4 columns instead of 2)
        Line #764 (got 3 columns instead of 2)
        Line #765 (got 3 columns instead of 2)
        Line #766 (got 3 columns instead of 2)
        Line #767 (got 3 columns instead of 2)
        Line #769 (got 3 columns instead of 2)
        Line #771 (got 3 columns instead of 2)
        Line #772 (got 3 columns instead of 2)
        Line #773 (got 3 columns instead of 2)
        Line #774 (got 3 columns instead of 2)
        Line #776 (got 3 columns instead of 2)
        Line #778 (got 3 columns instead of 2)
        Line #779 (got 4 columns instead of 2)
        Line #782 (got 3 columns instead of 2)
        Line #783 (got 3 columns instead of 2)
        Line #785 (got 3 columns instead of 2)
        Line #787 (got 3 columns instead of 2)
        Line #789 (got 4 columns instead of 2)
        Line #790 (got 3 columns instead of 2)
        Line #792 (got 4 columns instead of 2)
        Line #793 (got 4 columns instead of 2)
        Line #794 (got 3 columns instead of 2)
        Line #795 (got 4 columns instead of 2)
        Line #796 (got 4 columns instead of 2)
        Line #797 (got 3 columns instead of 2)
        Line #798 (got 6 columns instead of 2)
        Line #799 (got 3 columns instead of 2)
        Line #800 (got 4 columns instead of 2)
        Line #803 (got 4 columns instead of 2)
        Line #804 (got 3 columns instead of 2)
        Line #805 (got 3 columns instead of 2)
        Line #806 (got 3 columns instead of 2)
        Line #807 (got 4 columns instead of 2)
        Line #808 (got 4 columns instead of 2)
        Line #809 (got 3 columns instead of 2)
        Line #811 (got 3 columns instead of 2)
        Line #812 (got 3 columns instead of 2)
        Line #814 (got 3 columns instead of 2)
        Line #815 (got 5 columns instead of 2)
        Line #816 (got 3 columns instead of 2)
        Line #817 (got 3 columns instead of 2)
        Line #818 (got 4 columns instead of 2)
        Line #819 (got 4 columns instead of 2)
        Line #825 (got 3 columns instead of 2)
        Line #826 (got 3 columns instead of 2)
        Line #831 (got 3 columns instead of 2)
        Line #835 (got 3 columns instead of 2)
        Line #836 (got 3 columns instead of 2)
        Line #837 (got 8 columns instead of 2)
        Line #838 (got 4 columns instead of 2)
        Line #839 (got 3 columns instead of 2)
        Line #840 (got 1 columns instead of 2)
        Line #841 (got 3 columns instead of 2)
        Line #842 (got 3 columns instead of 2)
        Line #844 (got 3 columns instead of 2)
        Line #846 (got 3 columns instead of 2)
        Line #847 (got 3 columns instead of 2)
        Line #850 (got 4 columns instead of 2)
        Line #851 (got 3 columns instead of 2)
        Line #852 (got 4 columns instead of 2)
        Line #853 (got 4 columns instead of 2)
        Line #855 (got 5 columns instead of 2)
        Line #857 (got 3 columns instead of 2)
        Line #859 (got 3 columns instead of 2)
        Line #860 (got 3 columns instead of 2)
        Line #861 (got 3 columns instead of 2)
        Line #862 (got 3 columns instead of 2)
        Line #865 (got 3 columns instead of 2)
        Line #868 (got 3 columns instead of 2)
        Line #869 (got 5 columns instead of 2)
        Line #870 (got 3 columns instead of 2)
        Line #871 (got 4 columns instead of 2)
        Line #875 (got 3 columns instead of 2)
        Line #876 (got 4 columns instead of 2)
        Line #879 (got 3 columns instead of 2)
        Line #880 (got 3 columns instead of 2)
        Line #881 (got 3 columns instead of 2)
        Line #882 (got 3 columns instead of 2)
        Line #883 (got 3 columns instead of 2)
        Line #884 (got 3 columns instead of 2)
        Line #885 (got 3 columns instead of 2)
        Line #886 (got 3 columns instead of 2)
        Line #887 (got 4 columns instead of 2)
        Line #888 (got 4 columns instead of 2)
        Line #889 (got 3 columns instead of 2)
        Line #890 (got 3 columns instead of 2)
        Line #896 (got 3 columns instead of 2)
        Line #897 (got 3 columns instead of 2)
        Line #898 (got 7 columns instead of 2)
        Line #899 (got 3 columns instead of 2)
        Line #900 (got 3 columns instead of 2)
        Line #906 (got 3 columns instead of 2)
        Line #907 (got 3 columns instead of 2)
        Line #908 (got 7 columns instead of 2)
        Line #909 (got 3 columns instead of 2)
        Line #910 (got 3 columns instead of 2)
        Line #911 (got 3 columns instead of 2)
        Line #912 (got 3 columns instead of 2)
        Line #913 (got 4 columns instead of 2)
        Line #915 (got 3 columns instead of 2)
        Line #918 (got 3 columns instead of 2)
        Line #919 (got 3 columns instead of 2)
        Line #920 (got 3 columns instead of 2)
        Line #921 (got 3 columns instead of 2)
        Line #924 (got 3 columns instead of 2)
        Line #925 (got 5 columns instead of 2)
        Line #926 (got 3 columns instead of 2)
        Line #929 (got 3 columns instead of 2)
        Line #930 (got 3 columns instead of 2)
        Line #931 (got 3 columns instead of 2)
        Line #932 (got 5 columns instead of 2)
        Line #933 (got 4 columns instead of 2)
        Line #934 (got 4 columns instead of 2)
        Line #935 (got 3 columns instead of 2)
        Line #937 (got 4 columns instead of 2)
        Line #938 (got 3 columns instead of 2)
        Line #940 (got 3 columns instead of 2)
        Line #941 (got 3 columns instead of 2)
        Line #944 (got 3 columns instead of 2)
        Line #945 (got 3 columns instead of 2)
        Line #947 (got 3 columns instead of 2)
        Line #955 (got 3 columns instead of 2)
        Line #956 (got 3 columns instead of 2)
        Line #960 (got 3 columns instead of 2)
        Line #963 (got 3 columns instead of 2)
        Line #968 (got 3 columns instead of 2)
        Line #969 (got 3 columns instead of 2)
        Line #975 (got 3 columns instead of 2)
        Line #979 (got 4 columns instead of 2)
        Line #982 (got 4 columns instead of 2)
        Line #984 (got 4 columns instead of 2)
        Line #985 (got 3 columns instead of 2)
        Line #986 (got 3 columns instead of 2)
        Line #991 (got 3 columns instead of 2)
        Line #992 (got 3 columns instead of 2)
        Line #994 (got 4 columns instead of 2)
        Line #996 (got 4 columns instead of 2)
        Line #997 (got 4 columns instead of 2)
        Line #998 (got 3 columns instead of 2)
        Line #1002 (got 4 columns instead of 2)
        Line #1003 (got 3 columns instead of 2)
        Line #1006 (got 3 columns instead of 2)
        Line #1007 (got 3 columns instead of 2)
        Line #1011 (got 3 columns instead of 2)
        Line #1012 (got 3 columns instead of 2)
        Line #1013 (got 3 columns instead of 2)
        Line #1015 (got 5 columns instead of 2)
        Line #1016 (got 3 columns instead of 2)
        Line #1017 (got 3 columns instead of 2)
        Line #1019 (got 3 columns instead of 2)
        Line #1023 (got 4 columns instead of 2)
        Line #1024 (got 4 columns instead of 2)
        Line #1025 (got 4 columns instead of 2)
        Line #1026 (got 4 columns instead of 2)
        Line #1027 (got 5 columns instead of 2)
        Line #1028 (got 5 columns instead of 2)
        Line #1031 (got 4 columns instead of 2)
        Line #1032 (got 5 columns instead of 2)
        Line #1034 (got 4 columns instead of 2)
        Line #1036 (got 3 columns instead of 2)
        Line #1038 (got 3 columns instead of 2)
        Line #1039 (got 3 columns instead of 2)
        Line #1041 (got 3 columns instead of 2)
        Line #1049 (got 3 columns instead of 2)
        Line #1054 (got 4 columns instead of 2)
        Line #1057 (got 4 columns instead of 2)
        Line #1058 (got 3 columns instead of 2)
        Line #1060 (got 3 columns instead of 2)
        Line #1061 (got 3 columns instead of 2)
        Line #1062 (got 3 columns instead of 2)
        Line #1063 (got 4 columns instead of 2)
        Line #1064 (got 3 columns instead of 2)
        Line #1065 (got 3 columns instead of 2)
        Line #1066 (got 4 columns instead of 2)
        Line #1067 (got 3 columns instead of 2)
        Line #1068 (got 3 columns instead of 2)
        Line #1069 (got 3 columns instead of 2)
        Line #1073 (got 3 columns instead of 2)
        Line #1074 (got 3 columns instead of 2)
        Line #1075 (got 3 columns instead of 2)
        Line #1076 (got 3 columns instead of 2)
        Line #1080 (got 3 columns instead of 2)
        Line #1081 (got 4 columns instead of 2)
        Line #1084 (got 3 columns instead of 2)
        Line #1087 (got 3 columns instead of 2)
        Line #1089 (got 3 columns instead of 2)
        Line #1094 (got 3 columns instead of 2)
        Line #1100 (got 3 columns instead of 2)
        Line #1101 (got 3 columns instead of 2)
        Line #1102 (got 3 columns instead of 2)
        Line #1103 (got 4 columns instead of 2)
        Line #1104 (got 3 columns instead of 2)
        Line #1106 (got 4 columns instead of 2)
        Line #1109 (got 4 columns instead of 2)
        Line #1111 (got 5 columns instead of 2)
        Line #1112 (got 3 columns instead of 2)
        Line #1113 (got 3 columns instead of 2)
        Line #1114 (got 3 columns instead of 2)
        Line #1115 (got 3 columns instead of 2)
        Line #1117 (got 3 columns instead of 2)
        Line #1118 (got 3 columns instead of 2)
        Line #1119 (got 5 columns instead of 2)
        Line #1120 (got 3 columns instead of 2)
        Line #1121 (got 3 columns instead of 2)
        Line #1122 (got 4 columns instead of 2)
        Line #1123 (got 4 columns instead of 2)
        Line #1125 (got 3 columns instead of 2)
        Line #1127 (got 3 columns instead of 2)
        Line #1129 (got 6 columns instead of 2)
        Line #1130 (got 3 columns instead of 2)
        Line #1137 (got 3 columns instead of 2)
        Line #1141 (got 4 columns instead of 2)
        Line #1144 (got 3 columns instead of 2)
        Line #1145 (got 4 columns instead of 2)
        Line #1146 (got 3 columns instead of 2)
        Line #1147 (got 3 columns instead of 2)
        Line #1148 (got 3 columns instead of 2)
        Line #1149 (got 5 columns instead of 2)
        Line #1150 (got 4 columns instead of 2)
        Line #1151 (got 3 columns instead of 2)
        Line #1152 (got 3 columns instead of 2)
        Line #1153 (got 5 columns instead of 2)
        Line #1154 (got 4 columns instead of 2)
        Line #1155 (got 4 columns instead of 2)
        Line #1159 (got 3 columns instead of 2)
        Line #1161 (got 4 columns instead of 2)
        Line #1162 (got 4 columns instead of 2)
        Line #1163 (got 5 columns instead of 2)
        Line #1164 (got 3 columns instead of 2)
        Line #1167 (got 7 columns instead of 2)
        Line #1168 (got 3 columns instead of 2)
        Line #1169 (got 4 columns instead of 2)
        Line #1174 (got 3 columns instead of 2)
        Line #1175 (got 4 columns instead of 2)
        Line #1179 (got 3 columns instead of 2)
        Line #1181 (got 3 columns instead of 2)
        Line #1183 (got 4 columns instead of 2)
        Line #1186 (got 3 columns instead of 2)
        Line #1187 (got 3 columns instead of 2)
        Line #1191 (got 3 columns instead of 2)
        Line #1192 (got 3 columns instead of 2)
        Line #1194 (got 3 columns instead of 2)
        Line #1198 (got 3 columns instead of 2)
        Line #1199 (got 4 columns instead of 2)
        Line #1201 (got 1 columns instead of 2)
        Line #1202 (got 5 columns instead of 2)
        Line #1203 (got 4 columns instead of 2)
        Line #1204 (got 3 columns instead of 2)
        Line #1205 (got 4 columns instead of 2)
        Line #1206 (got 3 columns instead of 2)
        Line #1207 (got 3 columns instead of 2)
        Line #1209 (got 4 columns instead of 2)
        Line #1215 (got 3 columns instead of 2)
        Line #1217 (got 3 columns instead of 2)
        Line #1218 (got 3 columns instead of 2)
        Line #1219 (got 4 columns instead of 2)
        Line #1220 (got 4 columns instead of 2)
        Line #1221 (got 3 columns instead of 2)
        Line #1222 (got 5 columns instead of 2)
        Line #1223 (got 5 columns instead of 2)
        Line #1227 (got 3 columns instead of 2)
        Line #1228 (got 4 columns instead of 2)
        Line #1231 (got 3 columns instead of 2)
        Line #1232 (got 3 columns instead of 2)
        Line #1233 (got 4 columns instead of 2)
        Line #1235 (got 4 columns instead of 2)
        Line #1236 (got 4 columns instead of 2)
        Line #1240 (got 3 columns instead of 2)
        Line #1242 (got 3 columns instead of 2)
        Line #1245 (got 3 columns instead of 2)
        Line #1247 (got 3 columns instead of 2)
        Line #1250 (got 3 columns instead of 2)
        Line #1252 (got 4 columns instead of 2)
        Line #1253 (got 3 columns instead of 2)
        Line #1255 (got 3 columns instead of 2)
        Line #1257 (got 3 columns instead of 2)
        Line #1258 (got 3 columns instead of 2)
        Line #1261 (got 3 columns instead of 2)
        Line #1262 (got 3 columns instead of 2)
        Line #1263 (got 3 columns instead of 2)
        Line #1264 (got 3 columns instead of 2)
        Line #1268 (got 4 columns instead of 2)
        Line #1269 (got 3 columns instead of 2)
        Line #1270 (got 3 columns instead of 2)
        Line #1272 (got 3 columns instead of 2)
        Line #1273 (got 3 columns instead of 2)
        Line #1274 (got 3 columns instead of 2)
        Line #1276 (got 3 columns instead of 2)
        Line #1279 (got 4 columns instead of 2)
        Line #1281 (got 3 columns instead of 2)
        Line #1282 (got 3 columns instead of 2)
        Line #1283 (got 3 columns instead of 2)
        Line #1290 (got 3 columns instead of 2)
        Line #1291 (got 6 columns instead of 2)
        Line #1294 (got 7 columns instead of 2)
        Line #1295 (got 3 columns instead of 2)
        Line #1297 (got 3 columns instead of 2)
        Line #1298 (got 4 columns instead of 2)
        Line #1299 (got 4 columns instead of 2)
        Line #1300 (got 4 columns instead of 2)
        Line #1301 (got 4 columns instead of 2)
        Line #1303 (got 3 columns instead of 2)
        Line #1304 (got 3 columns instead of 2)
        Line #1306 (got 3 columns instead of 2)
        Line #1307 (got 3 columns instead of 2)
        Line #1309 (got 3 columns instead of 2)
        Line #1310 (got 3 columns instead of 2)
        Line #1317 (got 3 columns instead of 2)
        Line #1319 (got 3 columns instead of 2)
        Line #1325 (got 3 columns instead of 2)
        Line #1326 (got 3 columns instead of 2)
        Line #1327 (got 4 columns instead of 2)
        Line #1328 (got 3 columns instead of 2)
        Line #1333 (got 3 columns instead of 2)
        Line #1334 (got 3 columns instead of 2)
        Line #1337 (got 3 columns instead of 2)
        Line #1340 (got 4 columns instead of 2)
        Line #1343 (got 3 columns instead of 2)
        Line #1344 (got 3 columns instead of 2)
        Line #1346 (got 3 columns instead of 2)
        Line #1348 (got 3 columns instead of 2)
        Line #1349 (got 3 columns instead of 2)
        Line #1351 (got 4 columns instead of 2)
        Line #1353 (got 3 columns instead of 2)
        Line #1355 (got 3 columns instead of 2)
        Line #1356 (got 3 columns instead of 2)
        Line #1357 (got 3 columns instead of 2)
        Line #1359 (got 3 columns instead of 2)
        Line #1363 (got 3 columns instead of 2)
        Line #1365 (got 5 columns instead of 2)
        Line #1367 (got 3 columns instead of 2)
        Line #1368 (got 4 columns instead of 2)
        Line #1370 (got 3 columns instead of 2)
        Line #1373 (got 3 columns instead of 2)
        Line #1374 (got 6 columns instead of 2)
        Line #1377 (got 4 columns instead of 2)
        Line #1379 (got 3 columns instead of 2)
        Line #1380 (got 3 columns instead of 2)
        Line #1381 (got 3 columns instead of 2)
        Line #1382 (got 4 columns instead of 2)
        Line #1386 (got 3 columns instead of 2)
        Line #1387 (got 3 columns instead of 2)
        Line #1388 (got 4 columns instead of 2)
        Line #1391 (got 3 columns instead of 2)
        Line #1393 (got 3 columns instead of 2)
        Line #1394 (got 3 columns instead of 2)
        Line #1396 (got 3 columns instead of 2)
        Line #1397 (got 3 columns instead of 2)
        Line #1398 (got 3 columns instead of 2)
        Line #1399 (got 4 columns instead of 2)
        Line #1400 (got 5 columns instead of 2)
        Line #1401 (got 3 columns instead of 2)
        Line #1403 (got 5 columns instead of 2)
        Line #1404 (got 3 columns instead of 2)
        Line #1405 (got 4 columns instead of 2)
        Line #1406 (got 3 columns instead of 2)
        Line #1411 (got 3 columns instead of 2)
        Line #1417 (got 3 columns instead of 2)
        Line #1418 (got 3 columns instead of 2)
        Line #1420 (got 3 columns instead of 2)
        Line #1421 (got 4 columns instead of 2)
        Line #1422 (got 3 columns instead of 2)
        Line #1423 (got 3 columns instead of 2)
        Line #1424 (got 1 columns instead of 2)
        Line #1425 (got 3 columns instead of 2)
        Line #1428 (got 5 columns instead of 2)
        Line #1430 (got 3 columns instead of 2)
        Line #1431 (got 3 columns instead of 2)
        Line #1432 (got 4 columns instead of 2)
        Line #1434 (got 4 columns instead of 2)
        Line #1437 (got 3 columns instead of 2)
        Line #1439 (got 3 columns instead of 2)
        Line #1440 (got 4 columns instead of 2)
        Line #1441 (got 3 columns instead of 2)
        Line #1442 (got 3 columns instead of 2)
        Line #1443 (got 4 columns instead of 2)
        Line #1444 (got 4 columns instead of 2)
        Line #1445 (got 4 columns instead of 2)
        Line #1449 (got 4 columns instead of 2)
        Line #1450 (got 3 columns instead of 2)
        Line #1452 (got 3 columns instead of 2)
        Line #1454 (got 3 columns instead of 2)
        Line #1457 (got 3 columns instead of 2)
        Line #1459 (got 3 columns instead of 2)
        Line #1467 (got 3 columns instead of 2)



```python
'Targee Street Triangle\n'.split('\n')[0]
```




    'Targee Street Triangle'




```python
''.upper()
```




    ''




```python
len(str(int('100')))
```




    3




```python

```
