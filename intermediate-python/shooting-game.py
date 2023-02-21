"""Shooting Game

    You are creating a shooting game! The game has two types of enemies, aliens and monsters
    You shoot the aliens using your laser, and monsters using your gun. Each hit decreases the lives of the enemies by 1.

    The given code declares a generic Enemy class, as well as the Alien and Monster classes, with their corresponding lives count.
    It also defines the hit() method for the Enemy class.

    You need to do the following to complete the program:
    1. Inherit the Alien and Monster classes from the Enemy class.
    2. Complete the while loop that continuously takes the weapon of choice from user input and call the corresponding object's hit() method.

    Sample Input
    laser
    laser
    gun
    exit

    Sample Output
    The alien has 4 lives
    The alien has 3 lives
    The monster has 2 lives

"""


class Enemy:
    name = ""
    lives = 0

    def __init__(self, name, lives):
                self.name = name
                self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print('The ' + self.name + ' is dead')
        else:
            print('The ' + self.name + ' has '+ str(self.lives) + ' lives remaining')


class Monster(Enemy):
    def __init__(self):
        super().__init__('monster', 3)

    def hit(self):
        super().hit()


class Alien(Enemy):
    def __init__(self):
        super().__init__('alien', 5)

    def hit(self):
        super().hit()


monster = Monster()
alien = Alien()

while True:
    x = input("Enter a weapon (laser or gun) or exit: ")
    if x == 'exit':
        break
    elif x == 'laser':
        alien.hit()
    elif x == 'gun':
        monster.hit()
