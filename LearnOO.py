import random

TRAP_ARTISTS=[
    'Rickrose',
    'Henry Tihan',
    'Bobiwine',
    'Bebefool'
]

class TrapArtist:

    _hits=[
        'Mr Money',' Lovicaly','Work out','Sexy Lady'
    ]
    ##  double underscore is called dunder e.g dunder init.
    def __init__(self,name):
        #super().__init__()
        #OR Multipl inheritance
        ## Employee.__init__(self)
        #isinstance() issubclass()      
        self._name=name
        self._age=20

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name not in TRAP_ARTISTS:
            raise ValueError('%s not in trap airtists '%name)
        self._name=name

    @staticmethod
    def random_artists():
        return TrapArtist(random.choice(TRAP_ARTISTS)) 

    @classmethod 
    def hits(cls):
        return cls._hits


at=TrapArtist("Rickrose")
# print(at._name)
# at._name="Bebefool"
# print(at._name)

print(at.name)
at._name="Bebefool"
print(at.name)

print("### Random ..")
print(TrapArtist.random_artists().name)

print("Class Method")
print(TrapArtist.hits())
at._hits=['mr Katala','LOve everyday','African queen']
print(at._hits)
print(TrapArtist.hits())
at.__class__._hits=['mr Katala','LOve everyday','African queen']
print("New ----")
print(at._hits)
print(TrapArtist.hits())

at2=TrapArtist("Bobiwine")
print(at2.name)
print(at2._hits)


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
