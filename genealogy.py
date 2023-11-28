# Genealogy from https://usefulcharts.com/blogs/charts/star-wars-family-tree

class Person:
  def __init__(self, name):
    self.name = name
    self.mother = None
    self.father = None
    self.children = []

luke = Person("Luke Skywalker")
leia = Person("Leia Organa")
ben = Person("Ben Solo")
han = Person("Han Solo")
anakin = Person ("Anakin Skywalker")
padme = Person("Padme Amidala")

luke.father = anakin
luke.mother = padme

leia.father = anakin
leia.mother = padme

ben.mother = leia
ben.father = han


anakin.children.append(luke)
anakin.children.append(leia)

padme.children.append(luke)
padme.children.append(leia)

leia.children.append(ben)

han.children.append(ben)

