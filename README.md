# Smart Route Optimizer

A Python-based smart route optimization system that uses Dijkstra's algorithm to find optimal routes while considering traffic conditions.

## Features

- Find the shortest route between locations
- Traffic-aware route optimization
- Supports multiple locations and routes
- Displays all possible routes
- Calculates route distance
- Estimates travel time
- Estimates fuel cost
- Provides traffic analysis
- Visualizes the route network using NetworkX and Matplotlib
- Highlights the optimal route in the graph

## Technologies Used

- Python
- Dijkstra's Algorithm
- NetworkX
- Matplotlib
- Heapq

## How It Works

The system represents locations as nodes and roads as weighted edges in a graph. Dijkstra's algorithm is used to calculate the optimal route.

Traffic conditions such as Low Traffic, Medium Traffic, High Traffic, and Heavy Traffic are assigned additional weights. These traffic weights are considered while finding the optimal route.

## Project Flow

1. Select a source location.
2. Select a destination location.
3. The system analyzes available routes.
4. Traffic conditions are considered.
5. Dijkstra's algorithm finds the optimal route.
6. Distance, travel time, and fuel cost are calculated.
7. Traffic analysis is displayed.
8. The route network is visualized using NetworkX and Matplotlib.

## Locations

The system includes the following locations:

- Home
- Mall
- College
- Park
- Station
- Hospital
- Airport
- Office

## How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install networkx matplotlib

3. Run the program:
python smart_route_optimizer.py

4. Enter the source and destination locations when prompted.
##Project Highlights
This project demonstrates graph-based route optimization, Dijkstra's shortest path algorithm, traffic-aware routing, route analysis, and graph visualization using Python.
