#https://www.youtube.com/watch?v=oBt53YbR9Kk&t=5634s  Full

#Given an arayy and number n return if any numbers can in array can be added to make
#the number n

import re




def countSum(n, arr):
    if n == 0: 
        return True
    if n< 0: 
        return False
    for i in arr:
        remainder =n-i
        if countSum(remainder, arr):
            return True
    
    return False

def countSum_memo(n, arr):
    def count_sum_inner(n, arr,memo={}):
        if n in memo:
            return memo[n]
        if n == 0: 
            return True
        if n< 0: 
            return False
        for i in arr:
            remainder =n-i
            if countSum(remainder, arr):
                memo[n]=True
                return True

        memo[n]=False
        return False

    return count_sum_inner(n,arr)


# print ("countSum(7, [2,3,4,5])",countSum(7, [2,3,4,5]))
# print ("countSum(7, [9,3,8,5])",countSum(7, [9,3,8,5]))
#print ("countSum(300, [7,14])",countSum(300, [7,14]))

# print ("countSum_memo(7, [2,3,4,5])",countSum_memo(7, [2,3,4,5]))
# print ("countSum_memo(7, [9,3,8,5])",countSum_memo(7, [9,3,8,5]))
# print ("countSum_memo(300, [7,14])",countSum_memo(300, [7,14]))


#How many sums can add up a number
def howSum(targetSum,arr):#memo={}
    # if targetSum in memo:
    #     return memo[targetSum]

    if targetSum == 0:
        return []
    if targetSum<0:
        return None
    for i in arr:
        remainder=targetSum-i
        rs=howSum(remainder,arr)
        if rs is not None:
            #memo[remainder] =rs+[i]
            #return memo[remainder]
            return rs+[i]
    return None
#complexity check
#m=target sum
#n=items 
#time O(n^m *m)
#space O(m)

#memorized
#time: O(n*m^2)
#space: O(m^2)
print ("howSum(7,[2,3]) ",howSum(7,[2,3]))
print ("howSum(7,[5,3,4,7]) ",howSum(7,[5,3,4,7]))
print ("howSum(7,[2,4]) ",howSum(7,[2,4]))
print ("howSum(8,[2,3,5]) ",howSum(8,[2,3,5]))
print ("howSum(8,[3,5,2]) ",howSum(8,[3,5,2]))
# print("howSum(300,[7,14]) ",howSum(300,[7,14]) )

 #memo   
def how_sum_memo(target_sum,arr):
    def how_sum_memo_inner(target_sum,arr,memo={}):
        if target_sum in memo:
            #print ("Returning Memo: ",memo)
            return memo[target_sum]

        if target_sum == 0:
            return []
        if target_sum < 0:
            #print ("Returning None ",memo)
            return None

        for i in arr:
            remainder=target_sum-i
            #print("i=",i, "remainder=",remainder,"targetSum=",target_sum,arr)
            rs=how_sum_memo_inner(remainder,arr,memo)
            #print("i=",i, "remainder=",remainder,"targetSum=",target_sum,arr,"Result =",rs)
            if type(rs)==list :
                #combination = [*remainder_combination, num]
                memo[target_sum] =[*rs,i]
                #print ("memo[targetSum]",memo[target_sum],i)
                return memo[target_sum]
                #return rs+[i]

        memo[target_sum] =None
        return None
    return how_sum_memo_inner(target_sum,arr)

print ("how_sum_memo(7,[2,3]) ",how_sum_memo(7,[2,3]))
print ("how_sum_memo(7,[5,3,4,7]) ",how_sum_memo(7,[5,3,4,7]))
print ("how_sum_memo(7,[2,4]) ",how_sum_memo(7,[2,4]))
# print ("how_sum_memo(8,[2,3,5]) ",how_sum_memo(8,[2,3,5]))
# print ("how_sum_memo(8,[3,5,2]) ",how_sum_memo(8,[3,5,2]))
# print ("how_sum_memo(300,[7,14]) ",how_sum_memo(300,[7,14]) )


#Me task with no repeation   ??



#Best Sum Problem 
def best_sum(target_sum,arr):
    def best_sum_memo(target_sum,arr,memo={}):
        if target_sum in memo:
            return memo[target_sum]

        if target_sum==0:
            return []
        if target_sum <0:
            return None
        
        shortest_combination =None

        for i in arr:
            remainder=target_sum-i

            memo[target_sum]=best_sum_memo(remainder,arr,memo)

            if type(memo[target_sum])==list:
                combination= [*memo[target_sum],i]
                if shortest_combination is None or len(combination)<len(shortest_combination):
                    shortest_combination=combination

        memo[target_sum]=  shortest_combination  
        return memo[target_sum]
    return best_sum_memo(target_sum,arr)

print("best_sum(7,[5,3,4,7])",best_sum(7,[5,3,4,7]))
print("best_sum(8,[2,3,5])",best_sum(8,[2,3,5]))
# print("best_sum(8,[1,4,5])",best_sum(8,[1,4,5]))
# print("best_sum(100,[1,2,5,25])",best_sum(100,[1,2,5,25]))
# print("best_sum(100,[12,34])",best_sum(100,[12,34]))
# print("best_sum(1000,[12,45,50,12,100,124,34])",best_sum(1000,[12,45,50,12,100,124,34]))


#can COnstruct

def can_construct(target_str,arr):

    def can_construct_inner(target_str,arr,memo={}):
        if target_str in memo:
            return memo[target_str]

        if target_str =="":
            #print("Can't construct inner ",target_str)
            return True
        
        for i in arr:

            if target_str.startswith(i):
                newstr = target_str[len(i):]
                #print ("New string ",newstr)
                #result=can_construct(newstr,arr)
                memo[target_str]=can_construct_inner(newstr,arr,memo)
                if memo[target_str]:
                    return True

        memo[target_str] =False
        return False
    return can_construct_inner(target_str,arr)
    

# print("###can_construct###")
# print ("can_construct('position',['po','iom','mos','tion','me','sit','si'])",can_construct('position',['po','iom','mos','tion','me','sit','si']))
# print ("can_construct('positiony',['po','iom','mos','tion','me','sit','si'])",can_construct('positiony',['po','iom','mos','tion','me','sit','si']))
# print ("can_construct('positive',['po','iom','mos','tion','me','sit','si'])",can_construct('positive',['po','iom','mos','tion','me','sit','si']))
# print ("can_construct('process',['po','iom','mos','tion','me','sit','si','proce','ess','ss'])",can_construct('process',['po','iom','mos','tion','me','sit','si','proce','ess','ss']))
# print ("can_construct('behaviorow',['po','iom','mos','tion','me','sit','si','behav','beh','ioro','ow'])",can_construct('behaviorow',['po','iom','mos','tion','me','sit','si','behav','beh','ioro','ow']))
# print ("can_construct('eeeee',['p])",can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',[
# 'e',
# 'ee',
# 'eee',
# 'eeee',
# 'eeeee',
# 'eeeeee',
# 'eeeeeee']))


def count_construct(target_str, arr):

    def count_construct_inner(target_str, arr,memo={}):
        if target_str in memo:
            return memo[target_str]

        if target_str =='':
            return 1

        count = 0
        for i in arr:
            if target_str.startswith(i):
                memo[target_str]=count_construct_inner(target_str[len(i):], arr,memo)
                count+=memo[target_str]

        memo[target_str]=count
        return count
    return count_construct_inner(target_str,arr)


# print("###can_construct###")
# print ("count_construct('position',['po','iom','mos','tion','me','sit','si'])",count_construct('position',['po','iom','mos','tion','me','sit','si']))
# print ("count_construct('positiony',['po','iom','mos','tion','me','sit','si'])",count_construct('positiony',['po','iom','mos','tion','me','sit','si']))
# print ("count_construct('positive',['po','iom','mos','tion','me','sit','si'])",count_construct('positive',['po','iom','mos','tion','me','sit','si']))
# print ("count_construct('process',['po','iom','mos','tion','me','sit','si','proce','ess','ss'])",count_construct('process',['po','iom','mos','tion','me','sit','si','proce','ess','ss']))
# print ("count_construct('behaviorow',['po','iom','mos','tion','me','sit','si','behav','beh','ioro','ow'])",count_construct('behaviorow',['po','iom','mos','tion','me','sit','si','behav','beh','ioro','ow']))

# print("###HIM###")
# print ("count_construct('purple',['purp','p','ur','le','purpl'])",count_construct('purple',['purp','p','ur','le','purpl']))
# print ("count_construct('abcdef',['ab','abc','cd','def','abcd'])",count_construct('abcdef',['ab','abc','cd','def','abcd']))
# print ("count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar'])",count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
# print ("count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t'])",count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))

# print ("count_construct('eeeee',['p])",count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',[
# 'e',
# 'ee',
# 'eee',
# 'eeee',
# 'eeeee',
# 'eeeeee',
# 'eeeeeee']))


#All Construct Methods

def all_construct(target_str, arr):

    def all_construct_inner(target_str, arr,memo={}):
        if target_str in memo:
            return memo[target_str]

        if target_str =='':
            return [[]]

        possibleways = []
        for i in arr:
            if target_str.startswith(i):
                res=all_construct_inner(target_str[len(i):], arr,memo)
                #memo[target_str]=res #all_construct_inner(target_str[len(i):], arr,memo)
                #count+=memo[target_str]
                targetways=[ [i,*m] for m in res ]  #if len(m) > 0
                #memo[target_str]=targetways
                #if targetways:
                possibleways=possibleways+targetways
                # if memo[target_str]:
                #     possibleways.append([*possibleways,*memo[target_str],i])
                # else:
                #     possibleways.append([*possibleways,i])

        memo[target_str]=possibleways
        return possibleways
    l= all_construct_inner(target_str,arr)   
    return l,"Possible ways = ",len(l)


# print("###all_construct###")
print ("all_construct('purple',['purp','p','ur','le','purpl'])",all_construct('purple',['purp','p','ur','le','purpl']))
print ("all_construct('abcdef',['ab','abc','cd','def','abcd','ef','c])",all_construct('abcdef',['ab','abc','cd','def','abcd','ef','c']))
# print ("all_construct('skateboard',['bo','rd','ate','t','ska','sk','boar'])",all_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
# print ("all_construct('enterapotentpot',['a','p','ent','enter','ot','o','t'])",all_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))

# print ("all_construct('eeeee',['p])",all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',[
# 'e',
# 'ee',
# 'eee',
# 'eeee',
# 'eeeee',
# 'eeeeee',
# 'eeeeeee']))

#Tabulation strategy.
#Fibonaci

def fibonacci(n):
    table= [0 for i in range(n+1)]
    #print(table)
    table[1]=1
    for i in range(n+1):
        try:
            table[i+1]+=table[i]
            table[i+2]+=table[i]
        except IndexError as e:
            pass
            #print("Index error: " + str(e))

    return table[n]

#fibonacci Memorize
def fibonacci_memoize(n):

    def fibonacci_memoize_inner(n,memo={}):#memo={}
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        #return fibonacci_memoize_inner(n-1)+fibonacci_memoize_inner(n-2)
        memo[n]= fibonacci_memoize_inner(n-1,memo)+fibonacci_memoize_inner(n-2,memo)
        return memo[n]

    return fibonacci_memoize_inner(n)

print('fibonacci(6)',fibonacci(6))
print('fibonacci(7)',fibonacci(7))
print('fibonacci(8)',fibonacci(8))
print('fibonacci(50)',fibonacci(50))

print('fibonacci_memoize(6)',fibonacci_memoize(6))
print('fibonacci_memoize(7)',fibonacci_memoize(7))
print('fibonacci_memoize(8)',fibonacci_memoize(8))
print('fibonacci_memoize(50)',fibonacci_memoize(50))


#Grid traveller tabulation
def grid_traveller(m,n):
    table=[ [0]*m for _ in range(n) ]

    #table[1][1]=1#
    print(table)


    return ""

#print("grid_traveller(1,1)",grid_traveller(1,1))
#print("grid_traveller(2,3)",grid_traveller(2,3))
