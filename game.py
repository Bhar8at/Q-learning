import graphics
from sprite import sprite
import time 


class env():
    def __init__(self):
        self.matrix = graphics.matrix(5)
        self.character = sprite(" ^ ", self.matrix, "")
        self.checkpoint = sprite(" X ", self.matrix, "checkpoint")
        self.character.set_position()
        self.checkpoint.set_position()
        self.distance = (self.character.x - self.checkpoint.x)**2 + (self.character.y - self.checkpoint.y)**2
        
        self.score = 0
        self.steps = 0

    def state(self):
        self.state =   self.x + self.y * len(self.matrix)
        return self.state
    
    def reset(self):
        self.character.set_position()
        self.checkpoint.set_position()
        return self.state()

    def check_coincide(self):
        return self.character.x == self.checkpoint.x and self.character.y == self.checkpoint.y
    
    def step(self, action):
        if action == 0:
            self.character.move_up()
        elif action == 1:
            self.character.move_down()
        elif action == 2:
            self.character.move_left()
        elif action == 3:
            self.character.move_right()

        new_distance = (self.character.x - self.checkpoint.x)**2 + (self.character.y - self.checkpoint.y)**2
        if self.check_coincide():
            reward = 10
            done = True
        elif new_distance < self.distance:
            reward = 1
            done = False
        else:
            reward = -1
            done = False

        self.state = self.state()

        return self.matrix, reward, done
    
    def render(self):
        graphics.display(self.matrix)
        time.sleep(0.5)
        self.steps += 1
        if self.steps > 10:
            done = True
        else:
            done = False
        return done
    
    def possible_states(self):
        return len(self.matrix)**2




character_graphic = " ^ "
checkpoint_graphic = " X "
possible_actions = 4









if __name__ == "__main__":
    
    # Background intialization
    bg  = graphics.matrix(5)


    # Setting character and checkpoint positions
    character = sprite(character_graphic, bg)
    checkpoint = sprite(checkpoint_graphic, bg)
    character.set_position()
    checkpoint.set_position()

    
    graphics.display(bg)
    graphics.space()


