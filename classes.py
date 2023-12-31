class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def last_name(self):
        return self.name.split()[-1]
    
    def give_raise(self, persent):
        self.pay = int(self.pay * (1 + persent))
        
    def __str__(self):
        return '[Person: ' + self.name + ',' + str(self.pay) + ']'
    
class Manager(Person):
    def __init__(self, name, pay):
            Person.__init__(self, name, 'mgr', pay)
            
    def give_raise(self, percent, bonus=100):
            Person.give_raise(self, percent + bonus)
    
ivan = Person('Иван Иванович')
john = Person('Jon Sidorov', job='dev', pay=100000)

print(ivan.last_name())
print(john.last_name())
john.give_raise(.10)
print(john)

tom = Manager('Tom Jones', 50000)
tom.give_raise(0.10)
print(tom)


__name__
__module__
__dict__
__bases__
__doc__

###
__dict__
__class__
__init__
__del__
__cmp__
__hash__
__getattr__
__setattr__
__delattr__
__call__
###
__repr__
__str__
__oct__hex__complex__int__long__float__

