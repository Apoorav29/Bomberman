from person import Person
from wall import Wall


class Bomberman(Person):   # Inheritence of Person class in Bomberman class
    def __init__(self, char):
        Person.__init__(self, char)  # executes init function of Person class
