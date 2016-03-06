import curses.textpad

class Block:

    WIDTH = 16
    HEIGHT = 3

    def __init__(self, f, cell_y, cell_x):
        self.x = cell_x * self.WIDTH
        self.y = cell_y * self.HEIGHT
        self.f = f

    def draw(self, window):
        curses.textpad.rectangle(window, self.y, \
                                         self.x, \
                                         self.y + self.HEIGHT - 1, \
                                         self.x + self.WIDTH - 1)

        window.addnstr(self.y + 1, self.x + 1, self.f, self.WIDTH - 2)

    def destroy(self):
        pass #kill the file, destroy the block

    def top(self):
        return self.y

    def left(self):
        return self.x

    def bottom(self):
        return self.y + self.HEIGHT - 1

    def right(self):
        return self.x + self.WIDTH - 1

