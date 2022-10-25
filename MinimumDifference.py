# Given an unsorted array, find the minimum difference between any pair in the given array.
#also print the pairs leading to that difference

# Examples :

# Input: {1, 5, 3, 19, 18, 25}
# Output: 1
# Explanation: Minimum difference is between 18 and 19

# Input: {30, 5, 20, 9}
# Output: 4
# Explanation: Minimum difference is between 5 and 9

def findMinDiff(arr, n):
    # Initialize difference as infinite
    diff =( 10**20,())
 
    # Find the min diff by comparing difference
    # of all possible pairs in given array
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) < diff[0]:
                diff = (abs(arr[i] - arr[j]),(arr[i] , arr[j]))
 
    # Return min diff
    return diff


def findMinDiffv2(arr):
 
    # Sort array in non-decreasing order
    arr = sorted(arr)
 
    # Initialize difference as infinite
    diff =[]
 
    # Find the min diff by comparing adjacent
    # pairs in sorted array
    for i in range( len(arr)-1):
        if diff: 
            if arr[i+1] - arr[i] < diff[-1][0]:
                #diff.pop()
                diff=[]
                diff.append( (arr[i+1] - arr[i],(arr[i+1] , arr[i])))

            elif (arr[i+1] - arr[i]) == diff[-1][0]:
                print("Equal Adding Old= ",diff)
                diff.append((arr[i+1] - arr[i],(arr[i+1] , arr[i])))
                print("Equal Adding Old= ",diff)
        else:
            print("Initial value = ",diff)
            diff.append( ((arr[i+1] - arr[i]),(arr[i+1] , arr[i])))
            print("Initial value = ",diff)
 
    # Return min diff
    return diff


arr = [1, 5, 3, 19, 18, 25]
n = len(arr)

# Function call
print("Minimum difference is " + str(findMinDiffv2(arr)))

arr = [1, 5, 3, 19, 18, 25,30,31,50]
n = len(arr)

# Function call
print("Minimum difference is " + str(findMinDiffv2(arr)))