# Multi-AGV Scheduler

A multi-AGV warehouse scheduling and traffic control simulator.

## Project Goal

This project aims to build a simulation framework for multi-AGV/AMR task scheduling, path planning, conflict detection, traffic control, and deadlock handling in warehouse or factory environments.

## Main Features

- Grid / graph-based warehouse map modeling
- A* and Dijkstra path planning
- Multi-AGV task assignment
- Nearest-robot scheduler
- ETA-based scheduler
- Hungarian assignment scheduler
- Rolling scheduling framework
- OR-Tools based optimization baseline
- Reservation table for multi-robot conflict avoidance
- Vertex, edge, and swap conflict detection
- Deadlock detection based on wait-for graph
- Simulation metrics and visualization

## Project Structure

```text
multi-agv-scheduler/
├── configs/
├── maps/
├── core/
├── planner/
├── scheduler/
├── traffic/
├── evaluation/
├── visualization/
├── tests/
├── docs/
├── scripts/
└── main.py

