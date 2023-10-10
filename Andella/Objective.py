
#2
p=[[4,1],[2,3],[2,6]]
l=sorted(p, key=lambda x:[x[0],-x[1]])
print("IN ",p)
print(l)

#3 
print("#3")
def func(l):
    half=len(l)//2
    l[:]=l[half:]+l[:half]

l=[3,4,1,2]
print("IN ",l)
func(l)
print(l)

#5 set'
print([set() for _ in range(10)])
print([set()]*10)
#print(list(map(set,range(10))))
#print(list(map(set(),range(10))))
print(list(map(lambda x:set(),range(10))))
#print(list(map(lambda :set(),range(10))))

d = {"a": [1,2,3,4], "b": [5,6,7,8], "c": [9,10, 11,121]}
print(d)
#print(list (zip(d.values () )))
#[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
result = list(zip(d["a"], d["b"], d["c"]))
print(result)
     
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="22233344455566677778889999"
keypad=dict (zip(alph, num))
phone_number = "800-FOO-QUUX"
print("". join([keypad.get(x, x) for x in phone_number]))