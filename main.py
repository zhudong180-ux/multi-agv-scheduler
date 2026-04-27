import argparse
from typing import Tuple

from core.map_graph import GridMap
from planner.astar import AStarPlanner
from planner.dijkstra import DijkstraPlanner


def parse_position(values) -> Tuple[int, int]:
    return int(values[0]), int(values[1])


def build_planner(planner_name: str, grid_map: GridMap):
    if planner_name == "astar":
        return AStarPlanner(grid_map)

    if planner_name == "dijkstra":
        return DijkstraPlanner(grid_map)

    raise ValueError(f"Unsupported planner: {planner_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-AGV Scheduler: path planning demo"
    )

    parser.add_argument(
        "--map",
        type=str,
        default="maps/simple_warehouse.json",
        help="Path to warehouse map JSON file."
    )

    parser.add_argument(
        "--planner",
        type=str,
        default="astar",
        choices=["astar", "dijkstra"],
        help="Path planner type."
    )

    parser.add_argument(
        "--start",
        nargs=2,
        type=int,
        default=[0, 0],
        help="Start position: x y"
    )

    parser.add_argument(
        "--goal",
        nargs=2,
        type=int,
        default=[19, 19],
        help="Goal position: x y"
    )

    args = parser.parse_args()

    start = parse_position(args.start)
    goal = parse_position(args.goal)

    grid_map = GridMap.from_json(args.map)
    planner = build_planner(args.planner, grid_map)
    path = planner.plan(start, goal)

    print(f"planner: {args.planner}")
    print(f"map: {args.map}")
    print(f"start: {start}")
    print(f"goal: {goal}")
    print(f"path_found: {len(path) > 0}")
    print(f"path_length: {len(path)}")
    print("path:")
    print(path)


if __name__ == "__main__":
    main()
