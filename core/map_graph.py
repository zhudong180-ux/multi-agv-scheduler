import json
from typing import Iterable, List, Set, Tuple


Position = Tuple[int, int]


class GridMap:
    """
    Grid-based warehouse map.

    Coordinate convention:
    - position = (x, y)
    - x in [0, width)
    - y in [0, height)
    """

    def __init__(self, width: int, height: int, obstacles: Iterable[Position] = ()):
        self.width = width
        self.height = height
        self.obstacles: Set[Position] = {tuple(p) for p in obstacles}

    @classmethod
    def from_json(cls, file_path: str) -> "GridMap":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        width = int(data["width"])
        height = int(data["height"])
        obstacles = [tuple(item) for item in data.get("obstacles", [])]

        return cls(width=width, height=height, obstacles=obstacles)

    def in_bounds(self, pos: Position) -> bool:
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos: Position) -> bool:
        return pos not in self.obstacles

    def is_valid(self, pos: Position) -> bool:
        return self.in_bounds(pos) and self.passable(pos)

    def neighbors(self, pos: Position) -> List[Position]:
        x, y = pos
        candidates = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        return [p for p in candidates if self.is_valid(p)]
