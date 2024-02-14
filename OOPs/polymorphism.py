# Polymorphism refers to the occurance of something in multiple forms
#Using Polymorphism`:`
class French:
    def say_hello(self):
        print("Bonjour")

class Chinese:
    def say_hello(self):
        print("Ni hao")

def intro(lang):
    lang.say_hello()
    print("This is it")

Greg=French()
Leo=Chinese()

intro(Greg)

