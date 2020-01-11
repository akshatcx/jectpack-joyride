from config import all

class Character:
    
    def __init__(self, engine):
        
        #Check inheritance contructor
        
        _id = None
        _lives = 0
        _health = 0
        _size = [0, 0]
        _location = [0, 0]
        _velocity_y = -1 * GRAVITY

        right = 0
        left = 0
        down = 0
        up = 0
    
    @property
    def id(self):
        return _id
    
    @property
    def location(self):
        return _location
    
    @property
    def size(self):
        return _size

    def check_proximity(self, board):
        if location[1] + size[1] >= WIDTH:
            right = -1
        else:
            right=max(board[location[0]-size[0]+1:location[0]+1,location[1]+size[1]])

        if location[1] - 1 < 0:
            left = -1
        else:
            left = max(board[location[0]-size[0]+1:location[0]+1, location[1]-1])
        
        if location[0] - size[0] < 0:
            up = -1
        else:
            up = max(board[location[0] - size[0], location[1]:location[1] + size[1]])

        if location[0] + 1 >= HEIGHT:
            down = -1
        else:
            down = max(board[location[0] + 1,location[1]:location[1] + size[1]])
    
    def move(self, board, key,):
        
        if key == 'd':
            #Check if there is space on the right
            if right == 0:
                board[location[0] - size[0] + 1:location[0] + 1,location[1]] = [0] * size[0]
                board[location[0]-size[0]+1:location[0]+1,location[1]+size[1]] = [_id] * size[0]
                location[1] += 1

        if key == 'a':
            #Check if there is space on the left
            if left == 0:
                board[location[0]-size[0]+1:location[0]+1, location[1]+size[1]] = [0] * size[0]
                board[location[0]-size[0]+1:location[0]+1, location[1]-1] = [_id] * size[0]
                location[1] -= 1

        if key == 'w':
            _velocity_y += JUMP_VEL
            
        if _velocity_y > 0:
            #Check if there is space on the top
            if top == 0:
                board[location[0], location[1]:location[1] + size[1]] = [0] * size[1]
                board[location[0] - size[0], location[1]:location[1] + size[1]] = [_id] * size[1]
                location[0] -= 1
        
        elif _velocity_y < 0:
            #Check if there is space in the bottom
            if bottom == 0:
                board[location[0] - size[0] + 1,location[1]:location[1] + size[1]] = [0] * size[1]
                board[location[0] + 1,location[1]:location[1] + size[1]] = [_id] * size[1]
                location[0] += 1



