
import math
import os
import random
import re
import sys



#
# Complete the 'predictAnswer' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stockData
#  2. INTEGER_ARRAY queries
#

def predictAnswer(stockData, queries):
    # Write your code here
    days=[]
    for q in queries:
        #print("Check q= ",q)

        price= stockData[q-1]
        p1,p2=None,None
        haveError1,haveError2=False,False
        #print("Starting Inner For Loop ..",price," q = ",q)
        for idx in range(len(stockData)):
            #print("Inner Loop ..")
            if not haveError1:
                try:
                    iseach=q-2-idx
                    if iseach<0:
                        raise IndexError

                    prevp=stockData[q-2-idx]
                    #print("Previous Price ==",prevp,"Current == ",price)
                    if price>prevp:
                        #print("BReake Expected here ",q,prevp,'Index ',(1+idx))
                        p1= q-(idx+1)
                        break
                except IndexError as ee:
                    #print("Index eror P1, ", ee)
                    haveError1=True

            if not haveError2:
                try:
                    #print("Index check >> ",(q+idx)," q=",q," idx= ",idx)
                    afterp=stockData[q+idx]
                    if price >afterp:
                        p2=q+idx+1
                        
                        break
                except IndexError as e2:
                    #print("Index eror P2, ", e2)
                    haveError2=True
            
            if (haveError1 and haveError2):
                #print("Having Errors break..")
                break
            

        # for i in range(q-2,-1,-1):
        #     if price>stockData[i]:
        #         p1=i+1
        #         break
        # for i in range(q,len(stockData)):
        #     if price>stockData[i]:
        #         p2=i+1
        #         break

        #print("P1, P2 ",p1,p2)
        if p1 is not None and p2 is not None:
            #print(" q-p1= ",( q-p1)," q-p2 =",p2-q)
            if q-p1 > p2-q:
                #print("Adding p2 ")
                days.append(p2)
            else:
                #print("Adding p1 ")
                days.append(p1)

        elif p1 is None and p2 is not None:          
            days.append(p2)
        elif p2 is None and p1 is not None:
            days.append(p1)
       
        else:
            #print("Else Adding -1")
            days.append(-1)
    
    return days




if __name__ == '__main__':
    
    print("Starsing ...")
    # stockData=[5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    # queries = [3, 1, 8]

    # stockData=[5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    # queries = [6,5,4]

    stockData=[89214, 26671, 75144, 32445, 13656, 66289, 21951, 10265, 59857, 59133,
     63227, 86121, 37411,54628, 25859, 43510, 63756, 54763, 30852, 53243,
      76238, 96885, 33074, 17745, 81814, 43436, 79172, 92819, 30001, 68442,
       54021, 35566, 95113, 29164, 84362, 25120, 11804, 6313, 51736, 71661,
        81797, 14962, 57781, 35560, 85941, 99991, 95421, 66048, 54754, 26272,
         35642, 47343, 39508, 85068, 65087, 21321, 28503, 60611, 30491, 58503,
          29052, 84512, 94069, 40516, 13675, 78430, 65635, 25479, 1094, 17370,
           13491, 99243, 48683, 71271, 34802, 34624, 87613, 46574, 671, 42366,
            89197, 36313, 89708, 28704, 21380, 54795, 66376, 49882, 15405, 96867,
             24737, 60808, 81378, 35157, 1324, 11404, 29938, 66958, 53234, 47384]
    queries=[80, 24, 26, 62, 46, 79, 85, 59, 52, 8, 76, 48, 72, 84, 3, 3, 30, 30, 36, 86, 96, 72, 93, 25, 28, 68, 81, 18, 78, 14, 1, 57, 90, 26, 18, 87, 56, 55, 97, 59, 62, 73, 58, 85, 8, 60, 87, 89, 89, 22]

    result = predictAnswer(stockData, queries)

    print('\n'.join(map(str, result)))
   
