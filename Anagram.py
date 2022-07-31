

#countOfAnagramSubstring_old
#sherlockAndAnagrams_me
def countOfAnagramSubstring(s):
    # Write your code heref
    d={}
    for i in range(len(s)):
        an=""
        for j in range(i,len(s)):
            newstr=an+s[j]
            #print(newstr)
            arr=sorted(newstr)
            an = ''.join(arr)
            #print('After sorting == ',an)
            #d[an] = d.get(an, 0)+1
            d[an] = d[an]+1 if an in d else 1
    
    result=0
    print('Dict to check ',d)
    for k in d.keys():
        result+=( d[k]*(d[k]-1) )//2
    
    return result
        
    

def countOfAnagramSubstring_old(s):
    n = len(s)
    mp = dict()
     
    # loop for length of substring
    for i in range(n):
        sb = ''
        for j in range(i, n):
            print("sb + s[j] ",sb + s[j])
            sb = ''.join(sorted(sb + s[j]))
            mp[sb] = mp.get(sb, 0)

             
            # increase count corresponding
            # to this dict array
            mp[sb] += 1
 
    anas = 0
    print('MP==',mp)
    # loop over all different dictionary
    # items and aggregate substring count
    for k, v in mp.items():
        anas += (v*(v-1))//2
    return anas
 
# Driver Code

s = "xyyx"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))

s = "mom"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))

s = "abcd"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))

s = "abba"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))

s = "abba"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))

#ifailuhkqq
s = "ifailuhkqq"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))


s = "kkkk"
print("Testing Anagram == ",s)
print(countOfAnagramSubstring(s))


def countTriplets(arr, r):
    d = {}
    dicPairs = {}
    triple = 0

    reverse=list(reversed(sorted(arr)))
    for i in reverse:
        newmult=i*r
        if newmult in dicPairs:
            triple += dicPairs[newmult]

        if newmult in d:
            y =0 if i not in dicPairs else dicPairs[i] 
            dicPairs[i]=y+ d[newmult]

        d[i] =1 if i not in d else  d[i] + 1

    return triple

arr=[1, 5, 5, 25 ,125]
r=5
print("countTriplets  == ",arr,r)
print(countTriplets(arr,r))

#6 3
#1 3 9 9 27 81

arr=list(map(int,"1 3 9 9 27 81".split()))
r=3
print("countTriplets  == ",arr,r)
print(countTriplets(arr,r))

arr=list(map(int,"1 2 2 4".split()))
r=2
print("countTriplets  == ",arr,r)
print(countTriplets(arr,r))

#Ransom Note and Magazine
def checkMagazine(magazine, note):
    # Write your code here
    di = dict() # dict of word: count of that word in the note
    for n in note:
        di[n]=di.get(n,0)+1
       
    for m in magazine:
        if m in di:
            di[m] -= 1
            if di[m] == 0:
                del di[m]
                if  len(di)==0:
                    print("Yes")
                    return
    print("No") 

magazine ="give me one grand today night"
note = "give one grand today"
print("checkMagazine  == ",magazine,note)
checkMagazine(magazine,note)

magazine ="two times three is not four"
note = "two times two is four"
print("checkMagazine  == ",magazine,note)
checkMagazine(magazine,note)

magazine ="ive got a lovely bunch of coconuts"
note = "ive got some coconuts"
print("checkMagazine  == ",magazine,note)
checkMagazine(magazine,note)
