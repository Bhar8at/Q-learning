from random import randint

class sprite():
    
    def __init__(self, char, matrix, type):
        if type == "checkpoint":
            self.x = len(matrix)-1
            self.y = len(matrix)-1
        else:
            self.x = randint(0,len(matrix)-1)
            self.y = randint(0,len(matrix)-2)
        self.char = char
        self.background = matrix

    def move_up(self):
        if self.y - 1 in range(len(self.background)):
            self.y -=1

    def move_down(self):
        if self.y + 1 in range(len(self.background)):
            self.y +=1

    def move_right(self):
        if self.x + 1 in range(len(self.background)):
            self.x +=1

    def move_left(self):
        if self.x - 1 in range(len(self.background)):
            self.x -=1
    
    def set_position(self):
        self.background[self.y][self.x] = self.char


