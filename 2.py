# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:51:39 2019

@author: ESPraktikant
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:05:06 2018

@author: ESPraktikant
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.dates import strpdate2num
from functools import reduce
import matplotlib.dates as dates
import numpy as np
from collections import OrderedDict
from collections import defaultdict
import math
import re
import sys
import time
#from suffix_trees import STree
l=[]
dictionaryforMacAddress=defaultdict(dict)
dictionaryforFlexrayflags=defaultdict(dict)

prime = 101
listOfFrlines=[]
listOfETHlines=[]
listOfCANlines=[]
listOfFrotherlines=[]


ETHtimestamp=[]
ETHType=[]
ETHPayloaddata=[]
ETHslotIDlist=[]
ETHFrameHeader=[]

Frlineswithoutspace=[]
CANLineswithoutspace=[]
            
FrameHeaderforVLAN=[] 
Frwithoutspace=[]
l1=[]        
ETH=[]
FrPayloaddatalist=[]

class Dataseparation:
    
    def PassingfileasanArguement(self,f):
        for splittedlines in f:
            splittedlines=splittedlines.strip()
            if splittedlines.find("Fr")!=-1:     
               listOfFrlines.append(splittedlines.strip())  
            elif splittedlines.find("CAN")!=-1:    
                listOfCANlines.append(splittedlines.strip())
            elif splittedlines.find("ETH")!=-1:    
                listOfETHlines.append(splittedlines.strip())
            else:    
                listOfFrotherlines.append(splittedlines.strip())
        return listOfFrlines,listOfETHlines,listOfCANlines,listOfFrotherlines;
        
    def ETHdataseperation(self,list3=[], *args3):
        for ETHdata in list3:
            ETHdata=ETHdata.strip()
            ETHsplitteddata=ETHdata.split('  ')
            for i in range(1):
                if isinstance(float(ETHsplitteddata[0]), float):
                    ETHtimestamp.append(ETHsplitteddata[0])
                ETHType.append(ETHsplitteddata[i+1])
                ETHPayloaddata.append(ETHsplitteddata[i+2])
        return ETHtimestamp,ETHType,ETHPayloaddata;

    

    def ETHFramedelimetandHeader(self,list1=[], *args3):
        for data in list1:
            data=data.strip()
            ETHsplittedIdandframedata=data.split(':')
            for i in range(1):
                ETHslotIDlist.append(ETHsplittedIdandframedata[i])
                ETHFrameHeader.append(ETHsplittedIdandframedata[i+1])
        return ETHslotIDlist, ETHFrameHeader;
    


class RabinKrap:
    
    def search(self,pat, txt, q):
        d=256
        listindex=[]
        M = len(pat) 
        N = len(txt) 
        i = 0
        j = 0
        p = 0    
        t = 0    
        h = 1
      
        for i in range(M-1): 
            h = (h*d)%q 
  

        for i in range(M): 
            p = (d*p + ord(pat[i]))%q 
            t = (d*t + ord(txt[i]))%q 
  

        for i in range(N-M+1): 
        
            if p==t: 
                for j in range(M): 
                    if txt[i+j] != pat[j]: 
                        break
  
                j+=1
                if j==M:
                    listindex.append(i)
                    
  
            if i < N-M: 
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 
  
                if t < 0: 
                    t = t+q
        return listindex




        
        

class FindETHPattern(RabinKrap):
    def findETHpattern(self,ETHFrameHeader1,start,end):
        for line in ETHFrameHeader1:
            s = re.sub(r"\s+", "", line)
            Frwithoutspace.append(s)
        for l in Frwithoutspace:
            s=""
            for i in range(9,len(l)):
                s+=l[i]
            l1.append(s)
        prime=101
        p=0
        j=0
        pattern=""
        patternlist=[]
        temp=[]
        for text in ETHFrameHeader1:
            text=text.strip()
            splitteddata=text.split(' ')    
            pattern=""
            temp.clear()
            for k in range(start,end):
                pattern+=splitteddata[k]
            patternlist.append(pattern)
            if len(patternlist)==1:
                c=0
                for line in Frwithoutspace:
                        list1=self.search(pattern,line,prime)
                        if len(list1)!=0:
                            dictionaryforFlexrayflags[j][c]=list1
                         
                       
                        c+=1                 
            else:
                k=len(patternlist)
                a=k-1
                for s in range(a):
                    temp.append(patternlist[s]) 
                if patternlist[a] not in temp:
                    c1=0
                    for line1 in Frwithoutspace:
                        list2=self.search(patternlist[a],line1,prime)
                        if len(list2)!=0:
                            dictionaryforFlexrayflags[j][c1]=list2
                                
                        c1+=1 
                       
                else:
                    patternlist=list(OrderedDict.fromkeys(patternlist))
                    j-=1 
            j+=1
            
    
    
        print(patternlist)
       
        for item in dictionaryforFlexrayflags:       
            print("this pattern {} is occured during theses lines at index position of {} ".format(patternlist[p],dictionaryforFlexrayflags[item]))
            p+=1
        print(len(dictionaryforFlexrayflags))
        dictionaryforFlexrayflags.clear()
      
        
        
    
    
lines=[]
x=[]
def main():
    with open('C:/Users/ESPraktikant/file2.asc', 'r') as file:
        lines=file.readlines()
        x=lines[16:1000]    
    file.close()
  
    obj=Dataseparation()
   # obj1=RabinKrap()
 
    obj3=FindETHPattern()
    
    listOfFrline,listOfETHline,listOfCANline,listOfFrotherline = obj.PassingfileasanArguement(x)
    k=len(listOfFrline)+len(listOfETHline)+len(listOfCANline)+len(listOfFrotherline)
    print(k)
    
    for line in listOfFrline:
        s = re.sub(r"\s+", "", line)
        Frlineswithoutspace.append(s)
        

    for line in listOfCANline:
        s = re.sub(r"\s+", "", line)
        CANLineswithoutspace.append(s)
    
    #Fr=listOfFrline.copy()    
    ETHtimestamp,ETHType,ETHPayloaddata=obj.ETHdataseperation(listOfETHline)
    ETHslotIDlist,ETHFrameHeader= obj.ETHFramedelimetandHeader(ETHPayloaddata)
    
    obj3.findETHpattern(listOfFrline,17,18)
    

         
if __name__ == '__main__': 
    main()  





date,bid,ask = np.loadtxt('C:/Users/ESPraktikant/file1.asc', unpack=True,
                              delimiter=',',
                              converters={0:strpdate2num('%Y%m%d%H%M%S')})


def percentChange(startPoint,currentPoint):
    return (float(currentPoint-startPoint)/startPoint)*100.00
    



def patternFinder():
    '''
    The goal of patternFinder is to begin collection of %change patterns
    in the tick data. From there, we also collect the short-term outcome
    of this pattern. Later on, the length of the pattern, how far out we
    look to compare to, and the length of the compared range be changed,
    and even THAT can be machine learned to find the best of all 3 by
    comparing success rates.
    '''
    
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
        time.sleep(55)
        
        y+=1
        


    def graphRawFX():
    
    fig=plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    
    ax1.plot(date,percentChange(ask[0],ask),'r')
    ax1.xaxis.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))

    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1_2 = ax1.twinx()

    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g',alpha=.3)

    plt.subplots_adjust(bottom=.23)

    plt.show()###

    
    
    