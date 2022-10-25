def cost(B):
    # Write your code here
    max_sum=0
    a = [1] * len(B)
    for i,v in enumerate(B):
        if i>0:
            mx = max(B[i-1],v)
            print("max = ",mx)
            a[i]=mx if mx ==B[i] else 1
            a[i-1]=mx if mx ==B[i-1] else 1
            print(a)
            max_sum+=abs(a[i]-a[i-1])
    print(a)     
    return max_sum


B=list(map(int,"100 2 100 2 100".split()))
print(B," cost(B) ",cost(B))

B=list(map(int,"10 1 10 1 10".split()))
print(B," cost(B) ",cost(B))

B=list(map(int,"1 2 3".split()))
print(B," cost(B) ",cost(B))

#3 15 4 12 10
B=list(map(int,"3 15 4 12 10".split()))
print(B," cost(B) ",cost(B))

#4 7 9
B=list(map(int,"4 7 9".split()))
print(B," cost(B) ",cost(B))