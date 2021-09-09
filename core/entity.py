from core import actor

class Entity(actor.Actor):
    def __init__(self, name, x_pos, y_pos, char, map, walkable):
        super().__init__(name, map)
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._char = char
        self._walkable = walkable
    
    def get_x_pos(self):
        return self._x_pos
    
    def set_x_pos(self, new_x_pos):
        self._x_pos = new_x_pos
    
    def get_y_pos(self):
        return self._y_pos
    
    def set_y_pos(self, new_y_pos):
        self._y_pos = new_y_pos
    
    def get_char(self):
        return self._char
    
    def set_char(self, new_char):
        self._char = new_char
    
    def is_walkable(self):
        return self._walkable