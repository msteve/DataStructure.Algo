#Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.
# Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?
# Example
# Buy one share day one, and sell it day two for a profit of . Return .
# No profit can be made so you do not buy or sell stock those days. Return .
# Function Description
# Complete the stockmax function in the editor below.
# stockmax has the following parameter(s):
# prices: an array of integers that represent predicted daily stock prices
# Returns
# int: the maximum profit achievable



def stockmax(prices):
    # Write your code here
    #startv=prices[0]  1 3 1 2
    print(prices)
    profit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            #sell this 
            diff=prices[i]-prices[i-1] #=2  1
            
            if prices[i]>(prices[i-1]+profit):
                profit=prices[i]-(profit+prices[i-1])
            elif diff>profit:
                print("Profit here is diff= ",diff,"profit= ",profit)
                profit+=diff
                print("After Profit here is diff= ",diff,"profit= ",profit)
                            
    return profit


def stockmaxv2(prices):
    max_profit=max(prices)
    total_profit=[]
    max_pos=-1
    #max_found=False
    print("in ",prices)
    for i in range(len(prices)):
        if prices[i]==max_profit:
            max_pos=i

        if max_pos < 0:
            print("Max Pos: ", max_pos,"before ",prices[i-1])
            new_diff=max_profit-prices[i]
            total_profit.append(new_diff)
           
        elif max_pos>0:
            #print(max_pos,"getting new Max old= ",max_profit,"using ",prices[i:])
            max_profit=max(prices[i:])
            #print(" new Max  ",max_profit)
            new_diff=max_profit-prices[i]
            total_profit.append(new_diff)
        
        elif max_pos==0:
            return 0
    print("total_profit",total_profit)      
    return sum(total_profit)

def stockmaxv3(prices):
    print("In ",prices)
    m = prices[len(prices)-1]
    print("m=",m)
    max_sum = 0  
    sum_arr = 0
    reverse=reversed(prices)
    #reverse=iter(prices)
    print("reversed",reverse)
    for price in reverse:
        old=m
        m = max(m, price)
        print("Max of ",old, price,"= ",m)
        max_sum+=m 
        sum_arr+=price
        print("max_sum of ",max_sum,"sum arra= ",sum_arr)
    return max_sum-sum_arr
    

#1 3 1 2
prices=list(map(int,"5 3 2".split()))
#print("stockmax(prices)",stockmax(prices))
print("stockmaxv2(5 3 2)",stockmaxv2(prices))

prices=list(map(int,"1 3 1 2".split()))
print("stockmaxv2(1 3 1 2)",stockmaxv2(prices))

#1 2 100
prices=list(map(int,"1 2 100".split()))
print("stockmaxv2(1 2 100)",stockmaxv2(prices))

prices=list(map(int,"5 3 2".split()))
#print("stockmax(prices)",stockmax(prices))
print("stockmaxv3(5 3 2)",stockmaxv3(prices))

prices=list(map(int,"1 3 1 2".split()))
print("stockmaxv3(1 3 1 2)",stockmaxv3(prices))

#1 2 100
prices=list(map(int,"1 2 100".split()))
print("stockmaxv3(1 2 100)",stockmaxv3(prices))

