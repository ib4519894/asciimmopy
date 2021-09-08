
class Map:
    def __init__(self, width, height, default="#"):
        self._width = width
        self._height = height
        self._default = default
        self._grid = self._make_grid(self._width, self._height, self._default)

    def _make_grid(self, width, height, char):
        row = [char for x in range(width)]
        grid = [row for y in range(height)]
        return grid
    
    def get_map(self):
        out = ""
        for row in self._grid:
            for point in row:
                out = f"{out} {point}"
            out = f"{out}\n"
        return out
