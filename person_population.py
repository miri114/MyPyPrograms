class Person(object):

    population = 0

    def __init__(self):
        self.population += 1


p1 = Person
p2 = Person
p3 = Person
p4 = Person
p5 = Person

print(Person.population)
