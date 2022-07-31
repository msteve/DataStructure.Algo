import random

##1.  
def turn_into_another_function(fnc):
    
    return another_function


def another_function():
    
    print('another function')


@turn_into_another_function
def a_function():
    
    print('a function')
        
    
a_function()


##2. 
def power_of(arg):

    def decorator(fnc):

        def inner():

            return fnc() ** exponent

        return inner
    
    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@power_of(.5)
def random_odd_digit():
    
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())


##3.
class Elephant:
    
    def __init__(self, fnc):
        
        self._fnc = fnc
        self._memory = []
        
    def __call__(self):
        
        retval = self._fnc()
        self._memory.append(retval)
        return retval
    
    def memory(self):
        
        return self._memory


@Elephant
def random_odd_digit_class():
    
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit_class())
print(random_odd_digit_class.memory())
print(random_odd_digit_class())
print(random_odd_digit_class.memory())