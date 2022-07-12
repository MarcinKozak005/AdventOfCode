class Holder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set()
        self.store()

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == '>':
            self.x += 1
        elif direction == 'v':
            self.y -= 1
        else:  # '<'
            self.x -= 1

    def store(self):
        self.visited.add((self.x, self.y))


h = Holder()
data = open('03data.txt', 'r').read()

for d in data:
    h.move(d)
    h.store()
print(f'Santa visited: {len(h.visited)} houses')
