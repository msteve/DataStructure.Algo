

def gibonacci(n, x, y):
    #This is the base case when n==0
    if n==0:
        return x
    #base case when n==1
    if n==1:
        return y
    #base case done.
    #then call the function itsself
    return gibonacci(n-1,x,y)-gibonacci(n-2,x,y)

def gibonacciv2(n, x, y):
    #try:
    def gibonacci_memo(n, x, y,memo={}):
        #This is the base case when n==0\
        if n in memo:
            return memo[n]

        if n==0:
            return x
        #base case when n==1
        if n==1:
            return y
        #base case done.
        #then call the function itsself
        memo[n] =gibonacci_memo(n-1,x,y,memo)-gibonacci_memo(n-2,x,y,memo)
        return memo[n]
    return gibonacci_memo(n, x, y)

# print("gibonacci(0, 0, 1) = 0",gibonacci(0, 0, 1))
# print("gibonacci(1, 0, 1) = 1",gibonacci(1, 0, 1))
# print("gibonacci(2, 0, 1) = 1",gibonacci(2, 0, 1))
# print("gibonacci(3, 0, 1) = 0",gibonacci(3, 0,1))
# print("gibonacci(500, 5, 1) = 0",gibonacci(500, 5, 1))

print("gibonacciv2(0, 0, 1) = 0",gibonacciv2(0, 0, 1))
print("gibonacciv2(1, 0, 1) = 1",gibonacciv2(1, 0, 1))
print("gibonacciv2(2, 0, 1) = 1",gibonacciv2(2, 0, 1))
print("gibonacciv2(3, 0, 1) = 0",gibonacciv2(3, 0,1))
print("gibonacciv2(500, 5, 1) = 0",gibonacciv2(500, 5, 1))
print("gibonacciv2(900, 5, 1) = 0",gibonacciv2(900, 5, 1))