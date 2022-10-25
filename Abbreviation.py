from collections import Counter

def abbreviation(a, b):
    # Write your code here
    def abbreviation_memo(a, b,memo={}):
        if a in memo:
            return memo[a][0]
        
        if a.upper()==b.upper():
            return "YES"

        if a=="":
            return "YES"

        if str(a).islower():
            print("Memo ",memo)
            #print(memo)
            return "YES"
        #ABC
        for i in b:
            
            print("Checking  ",i," IN ",a)
            if i.upper() in a.upper():  #daBcd

                print("found ",i," IN ",a)
                newa=a.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                print("New==",newa)
                newb=b.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                memo[a]=(abbreviation_memo(newa,b,memo),newb)
                if memo[a][0]=="YES":
                    return "YES"

            # elif str(a).islower() and  :
            #     print("Everything Lower ",a)
            #     return "YES"

        return "NO"
    return abbreviation_memo(a,b)


def abbreviationv2(a, b):
    # Write your code here
    def abbreviation_memo(a, b,memo={}):
        if b in memo:
            return memo[b]
        if b=="":
            return "YES"
        
        if a.upper()==b.upper():
            return "YES"

        # if str(b).islower():
        #     return "YES"
        #ABC
        for i in a:
            
            print("Checking  ",i," IN ",b)
            if i.upper() in b.upper():  #daBcd
                print("found ",i," IN ",b)
                newb=b.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                print("New==",newb)
                memo[b]=abbreviation_memo(a,newb,memo)
                if memo[b]=="YES":
                    return "YES"
        return "NO"
    return abbreviation_memo(a,b)

#reduce both 
def abbreviationv3(a, b):
    # Write your code here
    def abbreviation_memo(a, b,memo={}):
        if b in memo:
            return memo[b]
        if b=="":
            return "YES"
        
        if a.upper()==b.upper():
            return "YES"

        if str(b).islower():
            return "YES"

        #ABC
        for i in a:
            
            print("Checking  ",i," IN ",b)
            if i.upper() in b.upper():  #daBcd
                print("found ",i," IN ",b)
                newb=b.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                print("New==",newb)
                newa=a.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                print("New== A==",newa)
                memo[b]=abbreviation_memo(newa,newb,memo)
                if memo[b]=="YES":
                    return "YES"
        return "NO"
    return abbreviation_memo(a,b)


def abbreviationv4(a, b):
    # Write your code here
    acounters =Counter(a.upper())
    bcounters =Counter(b.upper())
    diff=bcounters-acounters
    if len(diff)==0:
        return "YES"
    
    return "NO"

def abbreviation_newv1(a, b):
    # Write your code here
    acounters =Counter(a.upper())
    bcounters =Counter(b.upper())
    diff=bcounters-acounters
    if len(diff)==0:
        return "YES"
    
    return "NO"

def abbreviation_fromonline(a, b):
    # Write your code here
    def abbreviation_memo(a, b,memo={}):
        if a in memo:
            return memo[a][0]
        
        if a.upper()==b.upper():
            return "YES"

        if b=="":
            return "YES"

        if str(a).islower():
            print("Memo ",memo)
            #print(memo)
            return "YES"
        #ABC
        for i in b:
            print("Checking  ",i," IN ",a)
            if i.upper() in a.upper():  #daBcd

                print("found ",i," IN ",a)
                #newa=b.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                #print("New==",newa)
                newb=b.replace(i,"").replace(i.upper(),"").replace(i.lower(),"")
                memo[a]=(abbreviation_memo(a,newb,memo),newb)
                if memo[a][0]=="YES":
                    return "YES"

            # elif str(a).islower() and  :
            #     print("Everything Lower ",a)
            #     return "YES"

        return "NO"
    return abbreviation_memo(a,b)

print("abbreviation_fromonline(daBcd,ABC)",abbreviation_fromonline("daBcd","ABC"))
print("abbreviation_fromonline(daBcd,ABC)",abbreviation_fromonline("daBcd","ABC"))
print("abbreviation_fromonline(daBcd,ABC)",abbreviation_fromonline("daBcd","ABC"))
print("abbreviation_fromonline(AbCdE,AFE)",abbreviation_fromonline('AbCdE','AFE'))
print("abbreviation_fromonline('AfPZN','APZNC')",abbreviation_fromonline('AfPZN','APZNC'))
print("abbreviation_fromonline('KXzQ','K')",abbreviation_fromonline('KXzQ','K'))
print("abbreviation_fromonline('beFgH','EFG')",abbreviation_fromonline('beFgH','EFG'))
#beFgH EFG  
#print("abbreviationv2('beFgH','EFG')",abbreviationv2('beFgH','EFG'))
#print("abbreviation('beFgH','EFG')",abbreviation('beFgH','EFG'))
#print("abbreviation('AfPZN','APZNC')",abbreviation('AfPZN','APZNC'))

#print("abbreviationv4(daBcd,ABC)",abbreviationv4("daBcd","ABC"),"Expected YES")
#print("abbreviationv4('AfPZN','APZNC')",abbreviationv4('AfPZN','APZNC'),"Expected NO")


def candies(n, arr):
    # Write your code here
    candy_array=[]
    for i,r in enumerate(arr):
        if i==0:
            candy_array.append(1)
        else:
            if r>arr[i-1]:
                candy_array.append(candy_array[i-1]+1)
            else:
                candy_array.append(1)
    print(candy_array)           
    return sum(candy_array)
            

st=list(map(int,"10 2 4 2 6 1 7 8 9 2 1".split()))
print("st = ",st)
#print("candies(n,) ",candies(len(st),st))
