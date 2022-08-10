from itertools import combinations
import datetime

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    now=datetime.datetime.now()
    print("IN ",arr)
    n=len(arr)
    allnegatives=[r for i,r in enumerate(arr) if r<0 ]
    if len(allnegatives)==len(arr):
        return 0
    #non_adjacents=[]
    di={}
    maxsum=0
    for i,v in enumerate(arr):
        non_innner=[(v,i)]
        #non_innner_more=[(v,i)]
        for j,vv in enumerate(arr):
            if i!=j and j>i+1 :
                index=j-i
                if len(non_innner)>1:
                    if non_innner[-1][1]+1<j:
                        non_innner.append((vv,j))
                        di[str(index)+"_"+str(v)]=non_innner
                        print("non_innner 1=",non_innner)
                else:
                    non_innner.append((vv,j))
                    di[str(index)+"_"+str(v)]=non_innner
                    print("non_innner 2=",non_innner)
                 
            if j>i+1:
                if len(non_innner)>1:
                    newj=non_innner[-1][1]+1
                    new_index=newj-i
                    if n>newj:
                        #here
                        #di.get(new_index,[(v,i),(arr[newj],newj)])
                        key=str(new_index)+"_"+str(v)
                        if key in di:
                            oldv=di[key][-1]
                            newvalue=(arr[newj],newj)
                            print("Dict",di[key],"New Value =",newvalue,"old=",oldv)
                            if newvalue not in di[key]:
                                di[key ]= di[key]+[newvalue]
                        
                            
                        else:
                            di[key]=[(v,i),(arr[newj],newj)]
                            

    sumsall=[]
    allvalues=di.values()
    print("All values ",allvalues,"All DONE")
    
    for i in allvalues:
        li=[k[0] for k in i]
        for ii in range(2,len(li)+1):
            combs =combinations(li,ii)
            #print(combs,i)
            sums=[sum(i) for i in combs]
            print("Sums ",li,"= ",sums)
            sumsall=sumsall+sums

    now2=datetime.datetime.now()
    diff=now2-now
    print("**"*5,"Execution took ",diff.seconds,"seconds or ",diff.microseconds,"microseconds","**"*5)
        
    return max(sumsall)
    #return maxsum

def maxSubsetSumv2(arr):
    now=datetime.datetime.now()
    print("IN ",arr)
    n=len(arr)
    allnegatives=[r for i,r in enumerate(arr) if r<0 ]
    if len(allnegatives)==len(arr):
        return 0
    #non_adjacents=[]
    
    di={}
    maxsum=0
    for i,v in enumerate(arr):
        non_innner=[(v,i)]
        #non_innner_more=[(v,i)]
        for j,vv in enumerate(arr):
            if i!=j and j>i+1 :
                index=j-i
                if len(non_innner)>1:
                    if non_innner[-1][1]+1<j:
                        non_innner.append((vv,j))
                        di[str(index)+"_"+str(v)]=non_innner
                        print("non_innner 1=",non_innner)

                       
                else:
                    non_innner.append((vv,j))
                    di[str(index)+"_"+str(v)]=non_innner
                    print("non_innner 2=",non_innner)

                #try to get the sum max here
                #to AVoid check every time. First check if its the last index
                if (j+index)>=n:
                    local_items=[m[0] for m in non_innner]
                    print("Local Items =",local_items," Next Index would be  =",(j+index),"As compared to ",n)
                    sumslocal=[]
                    for ii in range(2,len(local_items)+1):
                        combs =combinations(local_items,ii)
                        sums=[sum(i) for i in combs if sum(i)>maxsum]
                        print("Sums Local= ",sums)
                        sumslocal=sumslocal+sums
                    if sumslocal: 
                        localmax=max(sumslocal)
                        if localmax>maxsum:
                            maxsum=localmax
                   
            if j>i+1:
                if len(non_innner)>1:
                    newj=non_innner[-1][1]+1
                    new_index=newj-i
                    if n>newj:
                        #here
                        #di.get(new_index,[(v,i),(arr[newj],newj)])
                        key=str(new_index)+"_"+str(v)
                        if key in di:
                            oldv=di[key][-1]
                            newvalue=(arr[newj],newj)
                            print("Dict",di[key],"New Value =",newvalue,"old=",oldv)
                            if newvalue not in di[key]:
                                di[key ]= di[key]+[newvalue]
                           
                        else:
                            di[key]=[(v,i),(arr[newj],newj)]

                        
                        if (j+new_index)>=n:
                            local_non_innner=di[key ]
                            local_items=[m[0] for m in local_non_innner]
                            print("Local Items 2 =",local_items," Next New Index would be =",(j+new_index),"As compared to ",n)
                            sumslocal=[]
                            for ii in range(2,len(local_items)+1):
                                combs =combinations(local_items,ii)
                                sums=[sum(i) for i in combs if sum(i)>maxsum]
                                print("Sums Local= ",sums)
                                sumslocal=sumslocal+sums
                            if sumslocal:
                                localmax=max(sumslocal)
                                if localmax>maxsum:
                                    maxsum=localmax

    now2=datetime.datetime.now()
    diff=now2-now
    print("**"*5,"Execution took ",diff.seconds,"seconds or ",diff.microseconds,"microseconds","**"*5)

    return maxsum


def maxSubsetSumv3(arr):
    now=datetime.datetime.now()
    print("IN ",arr)
    n=len(arr)
    allnegatives=(r for r in arr if r<0 )
    if len(list(allnegatives))==len(arr):
        return 0
    #non_adjacents=[]
    di={}
    maxsum=0
    new_dic={}
    skiplength=2
    #Attempt using dictionary instead of nested for loops
    for i,v in enumerate(arr):
        di_key=str(i)+"_"+str(v)
        new_v=(v,i)
        new_dic[di_key]=[new_v]
        if i>=skiplength:
            #get last added and increment
            #get previus 
            #if i%skiplength==0:
            #Assume on i=1, i=2..
            prev_indx=i-skiplength ##how to get previos
            if prev_indx>-1:
                prev_v=arr[i-skiplength]
                prev_key=str(i-skiplength)+"_"+str(prev_v)
                new_dic[prev_key]=new_dic[prev_key]+[new_v]


    print("=new_dic=",new_dic)  
    now2=datetime.datetime.now()
    diff=now2-now
    print("**"*5,"Execution took ",diff.seconds,"seconds or ",diff.microseconds,"microseconds","**"*5)

    return maxsum

def getMaxAndAssign(sumi,maxsum):
    result=sumi>maxsum
    maxsum=sumi
    return result
#arr = list(map(int, input().rstrip().split()))


def maxSubsetSum_recursive(arr):
    print("Arr ",arr)
    if len(arr)==0:
        return 0

    maxsum=0
    for i,elem in enumerate(arr):
        res,sum=0,0
        if i+2<len(arr):
            sum=elem+arr[i+2]
            newarr=arr[i+2:]
            res=maxSubsetSum_recursive(newarr)
            print("Current Sum ",sum," Max Sum ",maxsum)
        if sum>maxsum:
            print("Current Sum ",sum," Max Sum ",maxsum,"Assignig here ")
            maxsum+=sum
            print("### Having == ",maxsum)
            
        #print("New Array: " + str(newarr),maxsum)
        return res
        
        print("Max maxsum " , maxsum)
    

    return maxsum

def evaluate(indata,expected):
    arr = list(map(int, indata.rstrip().split()))
    #res = maxSubsetSumv3(arr)
    res = maxSubsetSum_recursive(arr)
    print("####### Sums max= Expected ",expected," Answer= ",res)


indata="3 7 4 6 5"
evaluate(indata,"13")

# indata="2 1 5 8 4"
# evaluate(indata,"11")

# indata="3 5 -7 8 10"
# evaluate(indata,"15")

# indata="5232 5859 2431 -4798 -4774 -7126 -1657 7743 -5529 -5855 3903 -2180 -1602 6777 -5136 -5800 -1242 3360 -4480 6968 3703 8163 -2391 -9601 7161 -3725 1787 5631 -2779 6607 7928 1011 -4715 -132 375 -4110 965 -9266 -7403 -9016 -517 -807 7710 4483 4361 -3218 -2060 -2608 -2978 8463 479 -8309 -6347 8945 6002 657 1741 3030 -6217 8566 -7492 5760 546 8073"
# evaluate(indata,"big")

# f="C:/Users/stephen.mbaalu/Downloads/input01.txt"
# indata=""
# with open(f) as ff:
#     indata=ff.read()
# #indata="3 7 4 6 5"
# evaluate(indata,"big")


