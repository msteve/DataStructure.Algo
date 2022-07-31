
import random
import time

def get_name():
    word='john moses simon henry steven carol sanyu darling'.split()
    print("Initial word ",word)
    try:
        while True:
            msg=yield word[random.randrange(0,len(word))]+" "+str(len(set(word)))
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

print("Calling Next")
nn=next(names)
print(nn)
print("Done calling next")
print(type(int(nn.split()[1])))
runs=0
while int(nn.split()[1])!=1:
    runs+=1
    nn=names.send(nn.split()[0])
    print(nn)
    time.sleep(0.5)

names.close()
print("Ran for ",runs," times")


# i=0
# for n in get_name():
#     print(n,"Resutl >>>")
#     i+=1
#     if i==10:
#         break



