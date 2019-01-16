# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:05:06 2018

@author: ESPraktikant
"""


from collections import OrderedDict
from collections import defaultdict
import math
import re
import sys
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
      
        
        
    
    

def main():
    with open('C:/Users/ESPraktikant/file2.asc', 'r') as file:
        lines=file.readlines()
        x=lines[16:1000]    
    file.close()
  
    obj=Dataseparation()
   
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

    
    
    