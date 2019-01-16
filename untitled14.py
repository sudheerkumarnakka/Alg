# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:37:58 2019

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




import matplotlib.cbook as cbook
totalStart = time.time()

datafile = cbook.get_sample_data('C:/Users/ESPraktikant/Desktop/GBPUSD1d.txt', asfileobj=False)
print('loading', datafile)


bid,ask = np.loadtxt(datafile,delimiter=',',skiprows=1, usecols=(0,2), unpack=True)



def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00
    



def patternFinder():
  
    
    #Simple Average
    avgLine = ((bid+ask)/2)
    
    #This finds the length of the total array for us
    x = len(avgLine)-30
    #This will be our starting point, allowing us to compare to the
    #past 10 % changes. 
    y = 11
    # where we are in a trade. #
    # can be none, buy,
    currentStance = 'none'
    while y < x:
        
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10= percentChange(avgLine[y-10], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        #function to account for the average of the items in the array
        print(reduce(lambda x, y: x + y, outcomeRange) / len(outcomeRange))

        
        print(currentPoint)
        print ('_______')
        print (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
       # time.sleep(55)
        
        y+=1

patternFinder()
        

        
