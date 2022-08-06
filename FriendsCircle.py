import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    di={}
    #total=0
    resultarr=[]
    donearr=[]
    for i,q in enumerate(queries):
        le=len(q)
        if i==0:
            resultarr.append(le)
            #total=le
            di[q[0]]={"q":(q,),"sum":le}
            di[q[1]]={"q":(q,),"sum":le}
        else:
            #if q[0] in di or q[1] in di:
            #localsum=0
            if q[0] in di and q[1] in di:
                print("Both Exists ",q,di[q[0]],di[q[1]],"DI=",di)
                newsum=di[q[0]]["sum"]+di[q[1]]["sum"]
                ##update backwards
                oldq=di[q[0]]["q"]#update each q.. last q
                #print("Old q 0= ",oldq)
                #print("di[oldq[-1]",di[oldq[-1][-1]])
                #print("di[oldq[-1][0]]",di[oldq[-1][0]])
                #print("di[oldq[-1][1]]",di[oldq[-1][1]])
                di[oldq[-1][0]]["sum"]=newsum
                di[oldq[-1][1]]["sum"]=newsum
                di[q[0]]={"q":(di[q[0]]["q"],q),
                "sum":newsum}
                
                oldq=di[q[1]]["q"]#update each q.. last q
                print("Old q 1= ",oldq)
                print("di[oldq[-1]",di[oldq[-1][-1]])
                di[oldq[-1][0]]["sum"]=newsum
                di[oldq[-1][1]]["sum"]=newsum
                
                di[q[1]]={"q":(di[q[1]]["q"],q),
                "sum":newsum}
                
                
                #new sum
                resultarr.append(newsum if newsum >resultarr[i-1] else resultarr[i-1])
                print("BothFd q[0]=",q[0],"SUM=",newsum, di[q[0]],"DI=",di)
                
                    
                
            elif q[0] in di or q[1] in di:
                    
                print("Eith Upper Exists ",q, (di[q[0]]if q[0] in di else di[q[1]]),"DI=",di)
                #condition this as well
                newsum=di[q[0]]["sum"]+1
                if q[0] in di:
                    oldq=di[q[0]]["q"]#update each q.. last q
                    print("Old Eith q 0= ",oldq)
                    #key=oldq[-1]
                    #if key in
                    #print(key,"Key ")
                    #print("Key=",key,"di[oldq[-1]",di[key])
                    if oldq[-1][0] in di:
                        print(oldq[-1][0])
                        di[oldq[-1][0]]["sum"]=newsum

                    if oldq[-1][1] in di:
                        print(oldq[-1][1])
                        di[oldq[-1][1]]["sum"]=newsum
                    
                    di[q[0]]= {"q":(di[q[0]]["q"],q),"sum":newsum}
                  
                if q[1] in di:
                    oldq=di[q[1]]["q"]#update each q.. last q
                    print("Old Eith q 1= ",oldq)
                    #key=oldq[-1]
                    #print(key,"Key ")
                    #print("Key=",key,"di[oldq[-1]",di[key])
                    di[oldq[-1][0]]["sum"]=newsum
                    di[oldq[-1][1]]["sum"]=newsum
                    di[q[1]]={"q":(di[q[1]]["q"],q),              "sum":newsum}
                resultarr.append(newsum if newsum >resultarr[i-1] else resultarr[i-1])
                #print("Eith Fd q=",q,"SUM=",newsum, di[q[0]],di[q[1]],"DI=",di)
                
                    
            # elif q[1] in di:
            #     localsum +=1
            #     di[q[1]]={"q":(di[q[1]]["q"],q),"sum":localsum}
            #     #resultarr.append(sumnew)
            #     print("Fd q[1]=",q[1],"SUM=",localsum, di[q[1]])
            #     resultarr.append(localsum)
            else:
                newsum=resultarr[i-1] if resultarr[i-1]>le else le
                di[q[0]]={"q":(q,),"sum":le}
                di[q[1]]={"q":(q,),"sum":le}
                resultarr.append(newsum )
                print("Non Fd q=",q,"SUM=",newsum, di[q[0]],di[q[1]],"DI=",di)
                
                
    return resultarr
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input())

    #queries = []

    #for _ in range(q):
    #    queries.append(list(map(int, input().rstrip().split())))
    queries = []
    s='G:/Work/me/study/pythLearn/Friends Data/input13.txt'
    with open(s) as ff:
        for l in ff:
            #indata=ff.readline()
            queries.append(list(map(int, l.split())))
    
    #print(queries)
    ans = maxCircle(queries)
    print('\n'.join(map(str, ans)))
