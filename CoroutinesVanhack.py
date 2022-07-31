def manipulate_generator(generator, n):
      # Enter your code here
    #print("## INI N ,",n)
    
    #print(((n!=2 and n!=3) and ( n%2==0 or n%3==0)))
    #t=generator()
    #next(generator)
    generator.send(None)
    if n==1:
        print("send n=1",generator.send(n))
    elif (n!=2 and n!=3) and ( n%2==0 or n%3==0):
        print("send n=",n,generator.send(n))
       
    

    # else:
    #     generator.send(None)
    #     print("#### NOT SENT ",n)

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
            #print("NOt None ==",x)
        else:
            n += 1
            #print("IS None ==",n)
print("Enter Value:")
k = int(input())
g = positive_integers_generator()
# mm=next(g)
# print(" Start MM ",mm)
for _ in range(k):
    #print("IN LOop ### ",_)
    n = next(g)
    print(" Print >>"*2,n)
    manipulate_generator(g, n)
