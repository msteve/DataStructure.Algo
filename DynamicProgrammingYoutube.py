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
# print ("howSum(7,[2,3]) ",howSum(7,[2,3]))
# print ("howSum(7,[5,3,4,7]) ",howSum(7,[5,3,4,7]))
# print ("howSum(7,[2,4]) ",howSum(7,[2,4]))
# print ("howSum(8,[2,3,5]) ",howSum(8,[2,3,5]))
# print ("howSum(8,[3,5,2]) ",howSum(8,[3,5,2]))
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
print ("how_sum_memo(8,[2,3,5]) ",how_sum_memo(8,[2,3,5]))
print ("how_sum_memo(8,[3,5,2]) ",how_sum_memo(8,[3,5,2]))
print ("how_sum_memo(300,[7,14]) ",how_sum_memo(300,[7,14]) )


#Me task with repeation   ??