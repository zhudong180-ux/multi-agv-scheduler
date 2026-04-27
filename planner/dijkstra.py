import heapq
from typing import Dict, List, Optional, Tuple

from core.map_graph import GridMap, Position


class DijkstraPlanner:
    def __init__(self, grid_map: GridMap):
        self.grid_map = grid_map

    def plan(self, start: Position, goal: Position) -> List[Position]:
        if not self.grid_map.is_valid(start):
            raise ValueError(f"Invalid start position: {start}")

        if not self.grid_map.is_valid(goal):
            raise ValueError(f"Invalid goal position: {goal}")

        open_heap = []
        heapq.heappush(open_heap, (0.0, start))

        came_from: Dict[Position, Optional[Position]] = {start: None}
        dist: Dict[Position, float] = {start: 0.0}

        while open_heap:
            current_dist, current = heapq.heappop(open_heap)

            if current == goal:
                return self._reconstruct_path(came_from, goal)

            if current_dist > dist[current]:
                continue

            for nxt in self.grid_map.neighbors(current):
                new_dist = current_dist + 1.0

                if nxt not in dist or new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    came_from[nxt] = current
                    heapq.heappush(open_heap, (new_dist, nxt))

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
