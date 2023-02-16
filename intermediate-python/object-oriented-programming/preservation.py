"""Preservation

    We are working on a game. Our Player class has name and private _lives attributes.
    The hit() method should decrease the lives of the player by 1.
    In case the lives equal to 0, it should output "Game Over".

    Complete the hit() method to make the program work as expected.
"""


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")


player = Player("Cyberpunk77", 3)

player.hit()
player.hit()
player.hit()
