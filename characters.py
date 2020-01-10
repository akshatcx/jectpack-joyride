from config import all

class Character:
    
    def __init__(self, engine):
        
        #Check inheritance contructor
        
        self.id = None
        self.engine = engine
        self.lives = 0
        self.health = 0
        self.size = [0, 0]
        self.location = [0, 0]
        self.velocity = [0, 0]

        self.right = 0
        self.left = 0
        self.down = 0
        self.up = 0

    def id(self):
        return id

    def location(self):
        return self.location

    def size(self):
        return self.size

    def x_vel(self, velocity):
        self.velocity[0] += velocity

    def y_vel(self, velocity):
        self.velocity[1] += velocity
    
    def check_proximity(self, board):
        
        
        

