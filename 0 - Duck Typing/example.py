def make_it_quack(duck):
    duck.quack()

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def bark(self):
        print("Woof!")

d = Duck()
make_it_quack(d)  # This prints "Quack!"

dog = Dog()
# make_it_quack(dog)  # This fails because Dog 
                      # doesn't have a method called "quack".
