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
cat.eat()         
        """
class Spam:
    num_of_insts = 0
  
    def __init__(self):
      Spam.num_of_insts = Spam.num_of_insts + 1

def print_num():
    print(Spam.num_of_insts)

a = Spam()
b = Spam()   
print_num()


      
