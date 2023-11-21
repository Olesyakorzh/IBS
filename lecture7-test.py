"""###
class Cat:
    def __init__(self):
        self.hungry = True
        
    def eat(self):
        if self.hungry:
            print('I am hungry!')
            self.hungry = False
        else:
            print("No!")
            
class Barsik(Cat):
    def __init__(self):
        super().__init__()
        self.sound = "Miu"
        print(self.sound)
        
cat = Barsik()
cat.eat()    """     

"""
class Spam:
    num_of_insts = 0
  
    def __init__(self):
      Spam.num_of_insts = Spam.num_of_insts + 1

def print_num():
    print(Spam.num_of_insts)

a = Spam()
b = Spam()   
print_num() """

"""
class Reverse:
    def __init__(self, data):
        self.data=data
        self.index=len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.data[self.index]
    
for ch in Reverse('12345'):
    print(ch)
    
rv = list(Reverse('12345'))
print(rv)   

"""
"""class Singleton(object):  
    def __new__(cls, *args, **kv):
        if not hasattr(cls, '_instance'):
            orig=super(Singleton, cls)
            cls._instance=orig.__new__(cls, *args, **kv)
        return cls._instance

a=Singleton()
print(id(a))
b=Singleton()
print(id(b))
        """ 
"""       
class Obj(object):
    __slots__ = ['a', 'b']
    
x = Obj()
x.a = 1
print(x.a)
"""
class Obj:
    def __call__(self, a):
        print(a)
        
    a=Obj()
    a(100)
    
    

    

      
