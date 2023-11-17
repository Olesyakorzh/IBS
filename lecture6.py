class Animal:
    
    def voice(self):
        pass
    
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


    

        
