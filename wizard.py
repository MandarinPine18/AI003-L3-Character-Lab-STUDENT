class Wizard:
    # ATTRIBUTES - add more as needed
    # you need to define the <name> attribute here - you should NOT change this anywhere besides the constructor

    # here's some attributes you might find useful as demonstrations - you can change these from anywhere you want
    strength: int = 0
    intelligence: int = 0
    stealth: int = 0

    # energy is an attribute unique to wizards which lets them cast spells - they always start at 100 and it gets lower every time they attack
    energy: int = 100

    # you need to define the <health> attribute here - this one should be changed using a method, NOT directly from outside the class

    # METHODS - add more as needed
    def __init__(self):
        pass  # replace this with your code - you will need to change the parameters of the constructor

    def get_info(self) -> str:
        return ""  # replace this with your code

    def get_health_string(self) -> str:
        return ""  # replace this with your code

    def attack(self, character):
        pass  # replace this with code to take 30 health off of <character> and take 20 energy off of <self>, printing a statement saying this wizard shot a fireball or cast a spell at the other character or something

    # ignore this method for now, we'll come back to it later
    def __str__(self):
        return super().__str__()
