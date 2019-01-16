
listt= [] 
FrameHeader0800=[]
FrameHeader002C=[]
FrameHeader004C=[]
FrameHeader0806=[]
FrameHeader0036=[]
FrameHeader88F7=[]
ETHpayloaddata=[] 
listt1=[]  
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
        p=0
        j=0
        prime=101
        #pattern=""
        patternlist=[]
        temp=[]
        for text in ETHFrameHeader1:
            pattern=""
            counter=0
            temp.clear()
            for k in range(start,end):
                pattern+=text[k]
            patternlist.append(pattern)
            if len(patternlist)==1:
                c=0
                for line in ETHFrameHeader1:
                    list1=self.search(pattern,line,prime)
                    if len(list1)!=0:
                        dictionaryforMacAddress[j][c]=list1
                        counter+=1
                    c+=1
            else:
                k=len(patternlist)
                a=k-1
                for s in range(a):
                    temp.append(patternlist[s])
                if patternlist[a] not in temp:
                    c1=0
                    for line1 in ETHFrameHeader1:
                        list2=self.search(patternlist[a],line1,prime)
                        if len(list2)!=0:
                            dictionaryforMacAddress[j][c1]=list2
                            counter+=1
                        c1+=1    
                else:
                    patternlist=list(OrderedDict.fromkeys(patternlist))
                    j-=1    
            j+=1
    
    
        print(patternlist)
        
        
        for item in dictionaryforMacAddress:       
            print("this pattern {} is occured during theses lines at index position of {} ".format(patternlist[p],dictionaryforMacAddress[item]))
            p+=1
        print(len(dictionaryforMacAddress))
        dictionaryforMacAddress.clear()
        
        
        
"""class FindFrpattern(RabinKrap):
    def Flexraypatternmatching(self,Frlines=[], *arg):
        q=0
        b=0
        string=""
        flexraypattern=[]
        temp1=[]
        for txt in Frlines:
            string=""
            counter1=0
            temp1.clear()
            for k2 in range(37,38):
                string+=txt[k2]
            flexraypattern.append(string)
            if len(flexraypattern)==1:
                c3=0
                for line2 in Frlines:
                    list4=self.pattern_matching(line2,string)
                    if len(list4)!=0:
                        dictionaryforFlexrayflags[b][c3]=list4
                        counter1+=1
                    c3+=1
            else:
                k1=len(flexraypattern)
                a1=k1-1
                for s1 in range(a1):
                    temp1.append(flexraypattern[s1])
                if flexraypattern[a1] not in temp1:
                    c2=0
                    for line6 in Frlines:
                        list6=self.pattern_matching(line6,flexraypattern[a1])
                        if len(list6)!=0:
                            dictionaryforFlexrayflags[b][c2]=list6
                            counter1+=1
                        c2+=1    
                else:
                    flexraypattern=list(OrderedDict.fromkeys(flexraypattern))
                    b-=1    
            b+=1
    
    
       # print(flexraypattern)
       
        for item in dictionaryforFlexrayflags:       
            print("this pattern {} is occured during theses lines at index position of {} ".format(temp1[q],dictionaryforFlexrayflags[item]))
            q+=1
        print(len(dictionaryforFlexrayflags))"""
        
        
        
        
    


def main():
    with open('C:/Users/ESPraktikant/file1.asc', 'r') as file:
        lines=file.readlines()
        x=lines[16:50000]    
    file.close()
  
    obj=Dataseparation()
   # obj1=RabinKrap()
    obj2=FindETHPattern()
   # obj3=FindFrpattern()
    
    listOfFrline,listOfETHline,listOfCANline,listOfFrotherline = obj.PassingfileasanArguement(x)
    k=len(listOfFrline)+len(listOfETHline)+len(listOfCANline)+len(listOfFrotherline)
    print(k)
    
    for line in listOfFrline:
        s = re.sub(r"\s+", "", line)
        Frlineswithoutspace.append(s) 
        

    for line in listOfCANline:
        s = re.sub(r"\s+", "", line)
        CANLineswithoutspace.append(s)
        
    ETHtimestamp,ETHType,ETHPayloaddata=obj.ETHdataseperation(listOfETHline)
    ETHslotIDlist,ETHFrameHeader= obj.ETHFramedelimetandHeader(ETHPayloaddata)
  
        
    for framedata in ETHFrameHeader:
        framedata=framedata.strip()
        str=""
        for i in range(40,44):
            str+=framedata[i]  
        if str=="0800":
            #TyperOfETH0800.append(str) 
            str1=""
            for j in range(44,len(framedata)):
                str1+=framedata[j]
            FrameHeader0800.append(str1)
        elif str=="002C":
            #TyperOfETH002C.append(str)
            str2=""
            for k in range(44,len(framedata)):
                str2+=framedata[k]
            FrameHeader002C.append(str2)   
        elif str=="004C":
            #TyperOfETH004C.append(str)
            str3=""
            for l in range(44,len(framedata)):
                str3+=framedata[l]
            FrameHeader004C.append(str3)
        elif str=="0806":
            #TyperOfETH0806.append(str)
            str4=""
            for m in range(44,len(framedata)):
                str4+=framedata[m]
            FrameHeader0806.append(str4)
        elif str=="0036":
            #TyperOfETH0036.append(str)
            str5=""
            for n in range(44,len(framedata)):
                str5+=framedata[n]
            FrameHeader0036.append(str5)
        elif str=="88F7":
            #TyperOfETH88F7.append(str)
            str6=""
            for o in range(44,len(framedata)):
                str6+=framedata[o]
            FrameHeader88F7.append(str6)
        
    
    
        
    
    #obj2.findETHpattern(ETHFrameHeader)
    
    #obj2.findETHpattern(ETHFrameHeader,12,24)
    #obj2.findETHpattern(ETHFrameHeader,24,28)
    #obj2.findETHpattern(ETHFrameHeader,32,36)
    #obj2.findETHpattern(ETHFrameHeader,40,44)
    #obj3.Flexraypatternmatching(Frlineswithoutspace)
 
    for data in FrameHeader0800:
        s=""
        s1=""
        start=40
        end=46
        for i in range(18,20):
            s+=data[i]
        listt.append(s)
        for j in range(start,end):
            s1+=data[j]
        listt1.append(s1)
            
            
    t=listt[0]
    i=1
    count=0
    for i in range(len(listt)):
        if t==listt[i]:
            count+=1
    print(count)
    print(len(FrameHeader0800))
    length=len(FrameHeader0800)
    
    t1=listt1[0]
    i1=1
    count1=0
    for i1 in range(len(listt1)):
        if t1==listt1[i1]:
            count1+=1
    print(count1)
    
    print(len(listt1))
    if count1>=100:
        print("this pattern {} is almost static during this index range{}-{}".format(t1,start,end))
    
        
            
        
if __name__ == '__main__': 
    main()  

    
    
    