# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:56:13 2019

@author: ESPraktikant
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:32:05 2019

@author: ESPraktikant
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from numpy import loadtxt
from matplotlib.dates import strpdate2num
from functools import reduce
import time
import datetime
import pandas as pd



#from matplotlib.mlab import load



import matplotlib.cbook as cbook
totalStart = time.time()

dataset = pd.read_csv('C:/Users/ESPraktikant/export_dataframe.csv')
dataset.head()


X=dataset.iloc[:, 0:12].values
Y=dataset.iloc[:,12].values
#x=pd.DataFrame(x)
#y=pd.DataFrame(y)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
LabelEncoder_X=LabelEncoder()
X[:,1]=LabelEncoder_X.fit_transform(X[:,1])

#Onehotencoder_x=OneHotEncoder(categorical_features=[0])
#Y=Onehotencoder_x.fit_transform(Y).toarray()
