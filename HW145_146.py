#Hometask_14_5 and Hometask_14_6

class Pet:
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self} бегает')

    def jump(self):
        print(f'{self} прыгает')

    def birthday(self):
        self.age += 1

    def sleep(self):
         print(f'{self} спит')

class Dog(Pet):
        def bark(self):
            print(f'{self} лает')

class Cat(Pet):
        def meow(self):
            print(f'{self} мяучит')

class  Parrot(Pet):
        def fly(self):
            print(f'{self} летает')



d = Dog("Жук",10,25)
print(d.name)
d.run()
d.jump()
print(d.age)
d.birthday()
print(d.age)
d.bark()
c = Cat("Пушистик",2,100)
c.run()
c.jump()
print(c.age)
c.birthday()
print(c.age)
c.meow()
p = Parrot("Гоша",25,100)
p.run()
p.jump()
print(p.age)
p.birthday()
print(p.age)
p.fly()