class animal:
    def eat(self):
        print("Animal eats food from mouth")
    def run(self):
        print("running..")

class dog(animal):
    def bark(self):
        print("dog barks")

class labrador(dog):
    def fight(self):
        print("fights..")

class monkey(animal):
    def eat(self):
        print("Monkey uses hands")
    def jump(self):
        print("jumps..")

a= animal()
a.eat()
a.run()

tommy= dog()
tommy.bark()
tommy.run()
tommy.eat()

l= labrador()
l.bark()
l.run()
l.eat()
l.fight()

m= monkey()
print(m.eat())
print(m.run())
print(m.jump())


class person:
    def gogym(self):
        print("Lift weights")
class pshake:
    def protein(self):
        print("drink pshake")

class bodybuilder(person, pshake):
    pass

someone= bodybuilder()
someone.gogym()
someone.protein()


class cars:
    def sedan(self):
        print("four doors")
    def engine(self):
        print("v4")

class jaguar:
    def engine(self):
        print("v6")

class audi:
    def type(self):
        print("suv")

