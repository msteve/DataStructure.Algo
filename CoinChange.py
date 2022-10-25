
import itertools

def getWays_old(n, c):

    def getWays_inner(n, arr,memo={}):

        if n==0:
            return [[]]
        if n<0:
            return None

        possibleways=[]

        for i in arr:
            remainder=n-i
            memo[n]=getWays_inner(remainder,arr,memo)
            if memo[n] is not None:
                #y=[*res,i ]
                #res = list(set(tuple(sorted(sub)) for sub in test_list))
                targetways=[sorted([i,*m]) for m in memo[n]]
                print(targetways)
            
                possibleways=possibleways+targetways
                #return y
        ans=possibleways #set(tuple(sorted(sub)) for sub in possibleways)
        print(ans)
        print("Len",len(ans))
        memo[n]=ans
        return memo[n]

    return len(getWays_inner(n, c))


def getWays(n, c):

    def getWays_inner(n, arr,currentCoint=0, memo={}):
        
        if n in memo:
            return memo[n]
        
        if n==0:
            return [[]]
        if n<0:
            return None

        possibleways=[]

        for i in range(currentCoint,len(arr)):
            remainder=n-arr[i]
            memo[n]=getWays_inner(remainder,arr,i, memo)
            print(i,arr[i]," res ",memo[n])
            if memo[n] is not None:
                #y=[*res,i ]
                #res = list(set(tuple(sorted(sub)) for sub in test_list))
                targetways=[[i,*m] for m in memo[n]]
                #print(targetways)
            
                possibleways=possibleways+targetways
                #return y
        ans=list(set(tuple(sorted(sub)) for sub in possibleways))
        #ans=possibleways
        #print(possibleways)
        #print(ans)
        #print("Len",len(ans))
        memo[n]=ans
        return memo[n]

    return len(getWays_inner(n, c))


#for explanation go to https://www.youtube.com/watch?v=DJ4a7cmjZY0 and read
def getWays_you(n, c):
    len_c = len(c)
    # num_rows = len_c + 1 # to account for when we have no coins ie coins = [] basecase
    num_rows = len_c + 1 # we need to account for empty coins case 
    if n == 0:
        return 1
    elif len_c == 0: # we now that n is not zero because of the above if case
        return 0
    
    num_cols = n+1 # to account for n=0 case
    cache = [] # cache is num_rows x num_cols 
    for i in range(num_rows):
        # have [] coins and try to sum up to n. There's one way, give no coins
        # so the first element of the first row is always 1
        row = [0] * num_cols
        row[0] = 1 # we try to sum to 0, so one way to do that, give no coins
        cache.append(row)

    print(cache)
    for i in range(1, num_rows): # first row is alwyas 1,0,0,0,0 ...n
        current_coins = c[:i]
        coin = current_coins[-1]
        for j in range(1,num_cols): # first col is always 1,1,1,1 ... num_rows
            col = j - coin
            # print(col)
                
            if col >= 0:
                cache[i][j] = cache[i-1][j] + cache[i][col]
            else:
                cache[i][j] = cache[i-1][j]
            # print(cache)
    return cache[-1][-1]


def combo(amount, c, currentCoin=0):
    #print("amount: ", amount,"c=",c)

    if n == 0:
        return 1
    
    if amount < 0:
        return 0
    
    nCombos = 0
    for i in range(currentCoin,len(c)):
        print(c[i])
        nCombos += combo(amount - c[i],c,i)
    
    
    return nCombos


def getWays_fromjava(n,c):

    def getWays_inner(n, c,current_coin,memo={}):
        if n in memo:
            return memo[n]

        if n == 0:
            return 1

        if n< 0:
            return 0

        combinations=0
        for i in range(current_coin,len(c)):
            #memo[n]=getWays_fromjava(n-c[i],c,i)
            remainder=n-c[i]
            #combinations+=getWays_inner(remainder,c,i,memo)
            res=getWays_inner(remainder,c,i,memo)
            #print(i,c[i]," result ",res)
            combinations+=res
            #memo[n]=combinations
            #print(memo)
          
        memo[n]=combinations
        print(memo)
        return combinations #memo[n]

    return getWays_inner(n, c,0)
	

def getWays_bruteforce(n, c,current_coin):
        if n == 0:
            return 1

        if n< 0:
            return 0

        combinations=0
        for i in range(current_coin,len(c)):
            #memo[n]=getWays_fromjava(n-c[i],c,i)
            combinations+=getWays_bruteforce(n-c[i],c,i)
            #combinations+=memo[n]
        return combinations


#1 2 3
li=list(map(int,"1 2 3".split()))
n=4
print("getWays(",n,",",li,")",getWays(n,li))

# print("getWays_bruteforce(",n,",",li,")",getWays_bruteforce(n,li))


li=list(map(int,"8 3 1 2".split()))
n=3
print("getWays(",n,",",li,")",getWays(n,li))
#print("getWays_bruteforce(",n,",",li,")",getWays_bruteforce(n,li))


li=list(map(int,"8 3 1 2".split()))
n=3
print("getWays(",n,",",li,")",getWays(n,li))
print("getWays_fromjava(",n,",",li,")",getWays_fromjava(n,li))


li=list(map(int,"3 25 34 38 26 42 16 10 15 50 39 44 36 29 22 43 20 27 9 30 47 13 40 33".split()))
n=222
print("getWays_fromjava(",n,",",li,")",getWays_fromjava(n,li))
#print("getWays_bruteforce(",n,",",li,")",getWays_bruteforce(n,li,0))
#print("getWays_you(",n,",",li,")",getWays_you(n,li))
#print("getWays(",n,",",li,")",getWays(n,li))

