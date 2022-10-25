

from hashlib import new
from operator import le


def equal_candies(arr):
    arr=sorted(arr)
    max=arr[-1]
    min=arr[0]

    target=None

    if max%2==0 or max%5==0:
        target=max
    else:
        target=max+1

    def equal_inner(arr,target,max,count):

        if len(set(arr))==1 and arr[0]==0:
            return arr

        

        if target!=max:
            #Attempt adding 1 on each candidate
            add=1
            max=target
        else:
            add=5 if  target-min>=5 else ( 2 if target-min>=2 else 1)

        print("Add is ",add)
        newarr=[]
        count+=count

        for i in arr:
            #if add ==1:
            #Adding 1 compulsory
            #should be 8-3
            t1=target-i
            if t1==0 or t1 in [1,2,5]:
                newarr.append(t1)
                print("Found Not added ",t1,i,target)
                if t1<=0:
                    return newarr
            else:
                t2=i+add
                t3=target-t2
                print(" added ",t2,i,target,t3)
                newarr.append(t3)
                if t3<=0:
                    return newarr


            # result=i+add
            # diff= target-result  #  8-4 =3
            # if diff not in [1,2,5] and diff <=target:
            #     newarr.append(result)
            # else:
            #     newarr.append(i)
        count+=1
        
        print(newarr)
        if len(set(newarr))==1 and newarr[0]==0:
            return (newarr,count)
        else:
            #recurssion
            #count=count
            return equal_inner(newarr, target,max,count)

        #return count

    return equal_inner(arr, target,max,0)



def equal_candiesv2(arr):
    #[10, 7, 12]
    print("***",arr)
    if len(set(arr))==1:
        return 1

    arr=sorted(arr)
    max=arr[-1]
    min=arr[0]

    target=None
    added_1=False
    if max%2==0 or max%5==0:
        target=max
    else:
        target=max+1
        added_1=True

    if added_1:
        add=1
    else:
        add=5 if  target-min>=5 else ( 2 if target-min>=2 else 1)
    newarr=[]
    count=1
    for i in arr:
        if added_1:
            #Adde add it
            #8-(7) =1 
            if i==max:
                print("I=max ,i=",i,"max=",max)
                newarr.append(i+add)

            elif target- i not in [1,2,5] and i!=max:
                print(" Added .. i= ",i,"add = ",add,"new su`m = ",add+i)
                newarr.append(i+add)
            else:
                print(" Not Added .. i= ",i,"add = ",add,"new su`m = ",add+i)
                newarr.append(i)
        else:

            if i==target:
                print("I and target equal i= ",i,"target",target)
                newarr.append(i)
            else:
                if i+add <=target:
                    print("I+Add = ",i,add,(i+add))
                    newarr.append(i+add)
                else:
                    print("I maintained ",i,"target",target)
                    newarr.append(i)
                #newarr.append()

    print("In array =",arr,"new array = ",newarr)
    if len(set(newarr))!=1:
        print("Set not yet 1.calling recursion ")
        return  count+equal_candiesv2(newarr)
        
    print("new array = ",newarr)
    return count

def equal_1(arr):
    # Write your code here
    max_arr = max(arr)
    min_arr = min(arr)
    diff = max_arr - min_arr
    count = 0
    increment = 0
    while(diff!=0):
        if diff >= 5:
            increment = 5
        elif diff < 5 and diff >=2:
            increment = 2
        else :
            increment = 1
        for i in range(0,len(arr)):
            if max_arr != arr[i]:
                arr[i] = arr[i] + increment
        count += 1
        max_arr = max(arr)
        min_arr = min(arr)
        diff = max_arr - min_arr
        print(max_arr , min_arr, diff, increment, arr)
    return count


def equal_2me(arr):
    arr=sorted(arr)
    max_value=arr[-1]# Assum 7
    min_value=arr[0] # 2

    target=None
    #added_1=False
    if max_value%2==0 or max_value%5==0:
        target=max_value
    else:
        target=max_value+1
        #added_1=True

    licount=[]

    for i in arr:
        diff=target-i # 8-2 =6
        print("target =",target,"i ",i,"diff ",diff)
        if diff%5==0:
            print("Diff ",diff,"Divisible by 5")
            licount.append(diff//5)
        
        else:
            print("Diff ",diff,"Not Divisible by 5")
            count=diff//5
            print("count  diff//5 ",count)
            remainder=diff%5
            print("count  diff//5 ",count,"remainder ",remainder)
            if remainder>=2:
                count+=(remainder//2)
                remainder2=remainder%2
                if remainder2>=1:
                    count+=1
            elif remainder >=1:
                count+=1

            licount.append(count)

    print(licount)
    result=max(licount)
    if result>1:
        return result
    else:
        #if len(licount)>1:
        return sum(licount)
     









# #li=list(map(int,"2 2 3 7".split()))
# #print("equal_candies(",li,")",equal_candies(li))
# print("###DOne Pair ###")
# li=list(map(int,"2 2 3 7".split()))
# print("equal_candiesv2(",li,")",equal_candiesv2(li))

# li=list(map(int,"2 2 3 7".split()))
# print("equal_1(",li,")",equal_1(li))

# #equal_1
# #10 7 12
# print("###DOne Pair ###")
# li=list(map(int,"10 7 12".split()))
# print("equal_candiesv2(",li,")",equal_candiesv2(li))

# li=list(map(int,"10 7 12".split()))
# print("equal_1(",li,")",equal_1(li))

# print("###DOne Pair ###")
# li=list(map(int,"1 1 5".split()))
# print("equal_candiesv2(",li,")",equal_candiesv2(li))

# li=list(map(int,"1 1 5".split()))
# print("equal_1(",li,")",equal_1(li))

# print("###DOne Pair ###")
# li=list(map(int,"1 1 5 15".split()))
# print("equal_candiesv2(",li,")",equal_candiesv2(li))

# li=list(map(int,"1 1 5 15".split()))
# print("equal_1(",li,")",equal_1(li))       

#new approach      
li=list(map(int,"2 2 3 7".split()))
print("equal_2me(",li,")",equal_2me(li))


li=list(map(int,"10 7 12".split()))
print("equal_2me(",li,")",equal_2me(li))

li=list(map(int,"1 1 5 15".split()))
print("equal_2me(",li,")",equal_2me(li))   

li=list(map(int,"1 1 5 15".split()))
print("equal_1(",li,")",equal_1(li)) 


li=list(map(int,"1 1 5".split()))
print("equal_2me(",li,")",equal_2me(li))

li=list(map(int,"1 1 5".split()))
print("equal_1(",li,")",equal_1(li))