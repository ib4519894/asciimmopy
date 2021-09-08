from core import entity
class Map:
    def __init__(self, width, height, empty_char="#"):
        self._width = width
        self._height = height
        self._default = empty_char
        self._grid = self._make_grid(self._width, self._height, self._default)

    def _make_grid(self, width, height, char):
        grid = [[entity.Entity("empty", x, y, "#", True) for x in range(width)] for y in range(height)]
        return grid
    
    def get_map(self):
        out = ""
        for row in self._grid:
            for point in row:
                out = f"{out} {point.get_char()}"
            out = f"{out}\n"
        return out

    def set_point(self, x_pos, y_pos, entity):
        out = []
        for y, old_row in enumerate(self._grid):
            row = []
            for x, old_value in enumerate(old_row):
                if x == x_pos and y == y_pos:
                    row.append(entity)
                    entity.set_x_pos(x_pos)
                    entity.set_y_pos(y_pos)
                else:
                    row.append(old_value)
            out.append(row)
        self._grid = out
