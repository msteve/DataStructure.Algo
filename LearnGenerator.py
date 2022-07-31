
import itertools
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        print("At start N= ",x)
        if x is not None:
            n = x
            print("NOt None ==",x)
        else:
            n += 1
            print("IS None ==",n)

pos=positive_integers_generator()
print(dir(pos))

y, y_backup = itertools.tee(pos)

print("calling NXET 1")
g=next(pos)
print(g)
print("calling NXET 2")
p=pos.send(10)
print("@@@@@ PP ",p)

print("sent 10 at  NXET 2")
g=next(pos)
print(g)
print("calling NXET 3")
g=next(pos)
print(g)

def generateItems(seq):
    for item in seq:
        y=yield 'item: %s' % item
        print("Just After Yield")
        print("Yield Values = ",y)


anIter = generateItems([])
#print 'dir(anIter):', dir(anIter)
anIter = generateItems([111,222,333])

# for x in anIter:
#     print (x)
#     print("DINE ",x)

# anIter = generateItems(['aaa', 'bbb', 'ccc'])
# print (anIter.next())
# print (anIter.next())
# print (anIter.next())
#print anIter.next()


DATA = [
'lemon',
'lime',
'grape',
'apple',
'pear',
'watermelon',
'canteloupe',
'honeydew',
'orange',
'grapefruit',
]

def make_producer(collection, excludes):
    gen = (item for item in collection if item not in excludes)
    print(type(gen))
    return gen

def test():
    iter1 = make_producer(DATA, ('apple', 'orange', 'honeydew', ))
    print ('%s' % iter1)
    print(type(iter1))
    for fruit in iter1:
        print (fruit)
#test()

#Generateor
m=(i for i in range(10) if i%2==0 )
#print(dir(m))
#print(type(m))
# print(m)
# print(next(m))
# print(next(m))
# print(next(m))

# print("TUPLE ")
# y=()
# print(dir(y))
# print(type(y))
# print(y)

def filter_and_transform(content, test_func,transforms=None):
    for x in content:
        if test_func(x):
            if transforms is None:
                yield x
            elif isiterable(transforms):
                for func in transforms:
                    x = func(x)
                    yield x
            else:
                yield transforms(x)

def isiterable(x):
    flag = True
    try:
        x = iter(x)
    except TypeError as exp:
        flag = False

    return flag

def iseven(n):
    return n % 2 == 0

def f(n):
    return n * 2

def g(n):
    return n ** 2

def test():
    data1 = [11, 22, 33, 44, 55, 66, 77, ]

    for val in filter_and_transform(data1, iseven, f):
        print ('val: %d' % (val, ))

    print ("-" * 40)

    for val in filter_and_transform(data1, iseven, [f,g]):
        print ('val: %d' % (val, ))

    print ("-" * 40)

    for val in filter_and_transform(data1, iseven):
        print ('val: %d' % (val, ))

# if __name__ == '__main__':
#     print("THis is New ###")
#     test()


import urllib
Urls = [
'http://google.com',
'http://python.org',
'http://gimp.org',
]
# The GNU image manipulation

def walk(url_list):
    for url in url_list:
        f = urllib.urlopen(url)
        stuff = f.read()
        f.close()
        yield stuff

def testv2():
    for x in walk(Urls):
        print ('length: %d' % (len(x), ))

# if __name__ == '__main__':
#     print("Ursls ###")
#     testv2()