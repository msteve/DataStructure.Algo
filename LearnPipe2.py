
import math

def producer(sentence, next_coroutine): 
    ''' 
    Producer which just split strings and 
    feed it to pattern_filter coroutine 
    '''
    tokens = sentence.split(" ") 
    for token in tokens: 
        next_coroutine.send(token) 
    next_coroutine.close() 

def producernumber(numlist, next_coroutine): 
    ''' 
    Producer which just split strings and 
    feed it to pattern_filter coroutine 
    '''
    
    for token in numlist: 
        next_coroutine.send(token) 
    next_coroutine.close() 




def squarer():
    # Write your code here

    try: 
        ans=0
        while True: 
            i=(yield ans)
            if i is not None:
                ans = math.sqrt(i) 
                print(ans) 
            #yield token
            #print(ans) 
    except GeneratorExit: 
        print("Done with printing!") 



def print_token(): 
    ''' 
    Act as a sink, simply print the 
    received tokens 
    '''
    print("I'm sink, i'll print tokens") 
    #print((yield),"previosu ##")

    try: 
        kk=""
        while True: 
            token = (yield) 
            print(token) 
            #yield token
            kk+=" "+token
            print(kk.strip())
            #token = (yield) 
            #print(token) 
    except GeneratorExit: 
        print("Done with printing!") 



def accumulatorv2():
    # Write your code here
    try: 
        ans=0
        while True: 
            i =(yield ans)
            if i is not None:
                ans+=i
              
    except GeneratorExit as ee: 
        print(ee)


def manipulate_generator(generator, n):
      # Enter your code here
      #print(n)
      #print(generator)
    if n=1:
        yield n
    elif n%2==0 or n%3==0
        yield n
        


  
# #pt = print_token() 
# pt= squarer()
# pt.__next__() 
# #pf = pattern_filter(next_coroutine = pt) 
# #pf.__next__() 
  
# sentence = "Bob is running behind a fast moving car"
# producer(sentence, pt) 


# pt= squarer()
# pt.__next__() 

numlist=[1,2,3]
#producernumber(numlist,pt)

# pt= accumulatorv2()
# next(pt)
# pt.send(3)
# next(pt)
#producernumber(numlist,pt)

pt= squarer()
for i in numlist:
    print(" InPUT ",i)
    next(pt)
    pt.send(i)
#next(pt)