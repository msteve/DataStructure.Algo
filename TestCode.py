def coro():
   print ('before yield')
   a = yield 'the yield value'
   print("### Yield A, ",a)
   b = yield a
   print("### Yield B, ",b)
   print ('done!')

c=coro() # this does not execute the generator, only creates it

 # If you use c.send('a value') here it could _not_ do anything with the value
 # so it raises an TypeError! Remember, the generator was not executed yet,
 # only created, it is like the execution is before the `print 'before yield'`

 # This line could be `c.send(None)` too, the `None` needs to be explicit with
 # the first use of `send()` to show that you know it is the first iteration
#print (next(c)) # will print 'before yield' then 'the yield value' that was yield
print("@ SENDING NONE ---")
#print(c.send(None))
print (next(c),'retuned')
print("@ SENDING NONE  DONE---")

print("@ SENDING 1st value ---")
print(c.send('first value sent'))  # will print 'first value sent'
print("@ SENDING 1st value DONE---")

 # will print 'done!'
 # the string 'the second value sent' is sent but not used and StopIterating will be raised
 # 
# print("@ SENDING last value ---")     
# print (c.send('the second value sent') )
# print("@ SENDING last value DONE---") 

#print (c.send('oops')) # raises StopIterating




prime_numbers = 0

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            #print(x,y,(x%y))
            if not ( x % y ):
                return False
    else:
	    return False
    #return True

def v2_isprime(n):

    def is_prime(n):
        if n >= 2:
            for i in range(2,n):
                #print(x,y,(x%y))
                if not ( n % i ):
                    return False
        else:
            return False
        return True

    return is_prime(n)

for i in range(int(input("How many numbers you wish to check: "))):
    if v2_isprime(i):
        prime_numbers += 1
        print(i)

print ("We found " + str(prime_numbers) + " prime numbers.")


