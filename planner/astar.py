import heapq
from typing import Dict, List, Optional, Tuple

from core.map_graph import GridMap, Position


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class AStarPlanner:
    def __init__(self, grid_map: GridMap):
        self.grid_map = grid_map

    def plan(self, start: Position, goal: Position) -> List[Position]:
        if not self.grid_map.is_valid(start):
            raise ValueError(f"Invalid start position: {start}")

        if not self.grid_map.is_valid(goal):
            raise ValueError(f"Invalid goal position: {goal}")

        open_heap = []
        heapq.heappush(open_heap, (0, start))

        came_from: Dict[Position, Optional[Position]] = {start: None}
        g_score: Dict[Position, float] = {start: 0.0}

        while open_heap:
            _, current = heapq.heappop(open_heap)

            if current == goal:
                return self._reconstruct_path(came_from, goal)

            for nxt in self.grid_map.neighbors(current):
                tentative_g = g_score[current] + 1.0

                if nxt not in g_score or tentative_g < g_score[nxt]:
                    g_score[nxt] = tentative_g
                    f_score = tentative_g + manhattan_distance(nxt, goal)
                    heapq.heappush(open_heap, (f_score, nxt))
                    came_from[nxt] = current

        return []

    @staticmethod
    def _reconstruct_path(
        came_from: Dict[Position, Optional[Position]],
        goal: Position
    ) -> List[Position]:
        path = []
        current: Optional[Position] = goal

        while current is not None:
            path.append(current)
            current = came_from[current]

        path.reverse()
        return path
