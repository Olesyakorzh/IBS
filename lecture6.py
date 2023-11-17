class Animal:
    
    def voice(self):
        pass
    num_of_insts = 0
    def __init__(self):
        Animal.num_of_insts = Animal.num_of_insts + 1
    
class Volf(Animal):
     def voice(self):
         print('Волк воет')
         

volf = Volf()
volf.voice()

class Fish(Animal):
    def voice(self):
        print('Рыба молчит')
        
fish = Fish()
fish.voice()

class Bird(Animal):
    def voice(self):
        print('Птичка поет')
        
bird = Bird()
bird.voice()

def print_num():
    print(Animal.num_of_insts)
    
print_num=staticmethod(print_num)

print_num()

        
