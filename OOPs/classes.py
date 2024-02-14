class Version:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
        
    


    def show(self):
        print("The name is ", self.make)

    def pirr(self):
        print("the model is ", self.model)





C1 =Version("Toyota","M2122",2021)

#using inheritace 

class animal:
    def __init__(self,name):
        self.name=name
   

    def speak(self):
        return
class Dog(animal):
    def speak(self):
        print(f"{self.name} says woaf")
class Cat(animal):
    def speak(self):
        print(f"{self.name} says meoaw")

Dxog=Dog("Rex")
Cxat=Cat("stripes")

Dxog.speak()
Cxat.speak()


        