import random
import time

def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    try :  
        while True: 
            print("Here Name FIrst  ==")
            name = (yield) 
            print("Here Name after Yeild ==",name)
            if prefix in name: 
                print("Prefix found =",name) 
            else: 
                print("Prefix not found =",name)
    except GeneratorExit as ex: 
        print("Closing coroutine!!",ex) 


# corou = print_name("Dear") 
# print("Declaring coroutine ** ",corou)
# y=next(corou)
# print("calling  coroutine ** ",y)
# h=corou.send("Dear")
# print("calling  coroutine ** ",h)
# m=corou.send("Mera")
# print("calling  coroutine 222 ** ",m)



def get_name():
    word='john moses simon henry steven carol sanyu darling'.split()
    print("Initial word ",word)
    try:
        while True:
            y=word[random.randrange(0,len(word))]+" "+str(len(set(word)))
            print("Here starting before yeild y =",y)
            msg=yield y
            print("Here  after Msg ==",msg)
            if msg is not None:
                print("New MSG ",msg)
                if msg!='carol':
                    word=['carol' if w==msg else w  for w in word ]
                
                print("New Word ",word)
            else:
                print("Nothing was sent so",word)
    except GeneratorExit as ee:
        print("Closed with ",ee)


print("Starting yeild function")
names=get_name()
print("Generator exp ",names)
print(" Calling Next ")
nn=next(names)
print(" Calling Next  result ",nn)

print(" Sending Moses ")
nn=names.send("Moses")
print(" Sending Moses  result ",nn)
print("Done calling next")
print(type(int(nn.split()[1])))

#names=get_name()