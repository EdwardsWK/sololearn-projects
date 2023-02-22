"""Name That Tune

    You are making a Music Player, which allows you to create a playlist of tracks.
    The given code defines Player and Track classes, where the Player is a linked list, chaining together Track objects.
    The code takes a number of tracks from user input and adds them to the playlist.

    You need to iterate over the linked list and output all the tracks in the playlist in the order of playback.
"""


class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next


class Player:
    def __init__(self):
        self.head = None

    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Track(title, None)


p = Player()

while True:
    x = input("Input a track name or input end to exit: ")
    if x == 'end':
        break
    p.add(x)

n = p.head

while n is not None:
    print(n.title)
    n = n.next

print()
