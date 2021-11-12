class Animal():

    def __init__(self, color, nr_of_legs):
        self.color = color
        self.nr_of_legs = nr_of_legs
        self.species = self.__class__.__name__

    def __repr__(self):
        return f'{self.color} {self.species}, ' \
               f'{self.nr_of_legs} legs'


class FourLeggedAnimal(Animal):

    def __init__(self):
        var = super().species
        self.nr_of_legs = 4


class Wolf(FourLeggedAnimal):

    def __init__(self, color):
        super().__init__()
        self.color = color

class Snake(Animal):

    def __init__(self, color):
        super().__init__(color, 0)


class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Parrot(Animal):

    def __init__(self, color):
        super().__init__(color, 2)


wolf = Wolf('black')
sheep = Sheep('white')
parrot = Parrot('green')
snake = Snake('brown')

print(wolf)
print(sheep)
print(snake)
print(parrot)