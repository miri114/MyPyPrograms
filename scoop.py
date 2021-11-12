class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor

""" This function is to create and print instances of class scoop"""
# def create_scoops():
#     scoops = [Scoop('chocolate'),
#               Scoop('vanilla'),
#               Scoop('persimmon')]
#
#     for scoop in scoops:
#         print(scoop.flavor)


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('persimmon')
s4 = Scoop('flavor4')
s5 = Scoop('flavor5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)

print(b)