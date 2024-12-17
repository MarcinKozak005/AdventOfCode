class Holder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0
        self.santa_turn = True
        self.visited = set()
        self.store()

    def move(self, direction):
        x = self.x if self.santa_turn else self.rx
        y = self.y if self.santa_turn else self.ry
        if direction == '^':
            y += 1
        elif direction == '>':
            x += 1
        elif direction == 'v':
            y -= 1
        else:  # '<'
            x -= 1

        if self.santa_turn:
            self.x, self.y = x, y
        else:
            self.rx, self.ry = x, y

    def store(self):
        x = self.x if self.santa_turn else self.rx
        y = self.y if self.santa_turn else self.ry
        self.visited.add((x, y))
        self.santa_turn = not self.santa_turn


h = Holder()
data = open('03data.txt', 'r').read()

for d in data:
    h.move(d)
    h.store()
print(f'Santa visited: {len(h.visited)} houses')
