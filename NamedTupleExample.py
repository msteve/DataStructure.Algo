# Python code to demonstrate namedtuple() and 
# Access by name, index and getattr() 

# importing "collections" for namedtuple() 
import collections 

# Declaring namedtuple() 
Student = collections.namedtuple('Student',['name','age','DOB']) 

# Adding values 
S = Student('Nandini',[2,34,4,55],'2541997') 

# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
print(type(S.age))

# Access using name 
print ("The Student name using keyname is : ",end ="") 
print (S.name) 

# Access using getattr() 
print ("The Student DOB using getattr() is : ",end ="") 
print (getattr(S,'DOB')) 


# # Adding values 
# S = Student('Nandini','19','2541997') 
  
# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
newstud=Student._make(li)
print (newstud) 
print(type(newstud.age))
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict()) 
  
# using ** operator to return namedtuple from dictionary 
print ("The namedtuple instance from dict is  : ") 
dicstud=Student(**di)
print (dicstud) 
print(type(dicstud.age))


# using _fields to display all the keynames of namedtuple() 
print ("All the fields of students are : ") 
print (S._fields) 
print(S.name)
  
# using _replace() to change the attribute values of namedtuple 
print ("The modified namedtuple is : ") 
print(S._replace(name = 'Manjeet')) 
print(dir(S))


import numpy as np 
import matplotlib.pyplot as plt 
  
# Returns a function that computes x ^ n for a given n 
def poly(n): 
    def polyXN(x): 
        return x**n 
    return polyXN 
  
# Functions to compare and colors to use in the graph 
FUNCTIONS = [np.log, poly(1), poly(2), poly(3), np.exp] 
COLORS = ['c', 'b', 'm', 'y', 'r'] 
  
# Plot the graphs  
def compareAsymptotic(n): 
    x = np.arange(1, n, 1) 
    plt.title('O(n) for n ='+str(n)) 
    for f, c in zip(FUNCTIONS, COLORS): 
        plt.plot(x, f(x), c) 
    plt.show() 
          
# compareAsymptotic(3) 
# compareAsymptotic(5) 
# compareAsymptotic(10) 
# compareAsymptotic(20) 