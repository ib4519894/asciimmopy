class Entity:
    def __init__(self, name, x_pos, y_pos, char, walkable):
        self.name = name
        self._x_pos = x_pos
        self._y_pos y_pos
        self._char = char
        self._walkable = walkable
    
    def get_x_pos(self):
        return self._x_pos
    
    def get_y_pos(self):
        return self._y_pos
    
    def is_walkable(self):
        return self._walkable