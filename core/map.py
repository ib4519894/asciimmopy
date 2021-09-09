from core import entity
class Map:
    def __init__(self, width, height, empty_char="#", actors=[]):
        self._width = width
        self._height = height
        self._default = empty_char
        self.actors = actors
        self._grid = self._make_grid(self._width, self._height, self._default)
        for actor in self.actors:
            self._turn(actor)

    def _make_grid(self, width, height, char):
        grid = [[char for x in range(width)] for y in range(height)]
        return grid
    
    def get_map(self):
        out = ""
        for row in self._grid:
            for point in row:
                out = f"{out} {point}"
            out = f"{out}\n"
        return out

    def set_point(self, x_pos, y_pos, char):
        out = []
        for y, old_row in enumerate(self._grid):
            row = []
            for x, old_value in enumerate(old_row):
                if x == x_pos and y == y_pos:
                    row.append(char)
                else:
                    row.append(old_value)
            out.append(row)
        self._grid = out
    
    def _turn(self, actor):
        actor.action()
