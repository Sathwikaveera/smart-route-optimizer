import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time

# =========================================================
# SMART ROUTE OPTIMIZER USING DIJKSTRA ALGORITHM
# =========================================================

# ---------------------------------------------------------
# GRAPH WITH MULTIPLE ROUTES
# ---------------------------------------------------------

graph = {

    'Home': [('Mall', 4), ('College', 2), ('Park', 6)],

    'Mall': [('Office', 5), ('Station', 3), ('Hospital', 7)],

    'College': [('Office', 1), ('Park', 2), ('Hospital', 4)],

    'Park': [('Office', 1), ('Airport', 8)],

    'Station': [('Office', 2), ('Airport', 3)],

    'Hospital': [('Airport', 2)],

    'Airport': [('Office', 4)],

    'Office': []

}

# ---------------------------------------------------------
# TRAFFIC CONDITIONS
# ---------------------------------------------------------

traffic = {

    ('Home', 'Mall'): 'High Traffic',
    ('Home', 'College'): 'Low Traffic',
    ('Home', 'Park'): 'Medium Traffic',

    ('Mall', 'Office'): 'High Traffic',
    ('Mall', 'Station'): 'Medium Traffic',
    ('Mall', 'Hospital'): 'Heavy Traffic',

    ('College', 'Office'): 'Low Traffic',
    ('College', 'Park'): 'Low Traffic',
    ('College', 'Hospital'): 'Medium Traffic',

    ('Park', 'Office'): 'Low Traffic',
    ('Park', 'Airport'): 'High Traffic',

    ('Station', 'Office'): 'Medium Traffic',
    ('Station', 'Airport'): 'Low Traffic',

    ('Hospital', 'Airport'): 'Medium Traffic',

    ('Airport', 'Office'): 'Low Traffic'
}

# ---------------------------------------------------------
# TRAFFIC WEIGHT VALUES
# ---------------------------------------------------------

traffic_weights = {

    'Low Traffic': 0,
    'Medium Traffic': 2,
    'High Traffic': 4,
    'Heavy Traffic': 6
}

# =========================================================
# DIJKSTRA ALGORITHM
# =========================================================

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}

    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node]:

            # TRAFFIC EFFECT

            traffic_condition = traffic.get(
                (current_node, neighbor),
                'Low Traffic'
            )

            extra_weight = traffic_weights[traffic_condition]

            distance = current_distance + weight + extra_weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances, previous

# =========================================================
# FIND SHORTEST PATH
# =========================================================

def get_path(previous, destination):

    path = []

    while destination:

        path.insert(0, destination)

        destination = previous[destination]

    return path

# =========================================================
# FIND ALL POSSIBLE ROUTES
# =========================================================

def find_all_routes(graph, start, end, path=[]):

    path = path + [start]

    if start == end:

        return [path]

    routes = []

    for neighbor, weight in graph.get(start, []):

        if neighbor not in path:

            new_routes = find_all_routes(
                graph,
                neighbor,
                end,
                path
            )

            for route in new_routes:

                routes.append(route)

    return routes

# =========================================================
# CALCULATE ROUTE DISTANCE
# =========================================================

def calculate_distance(route):

    total = 0

    for i in range(len(route)-1):

        current = route[i]

        nxt = route[i+1]

        for neighbor, weight in graph[current]:

            if neighbor == nxt:

                total += weight

    return total

# =========================================================
# DISPLAY INTRODUCTION
# =========================================================

print("\n================================================")
print("     SMART ROUTE OPTIMIZER SYSTEM")
print("================================================")

print("\nAvailable Locations:\n")

for place in graph:

    print("•", place)

# =========================================================
# USER INPUT
# =========================================================

source = input(
    "\nEnter Source Location : "
).title()

destination = input(
    "Enter Destination Location : "
).title()

# =========================================================
# VALIDATION
# =========================================================

if source not in graph or destination not in graph:

    print("\nInvalid Location Entered!")

else:

    # =====================================================
    # EXECUTION TIME START
    # =====================================================

    start_time = time.time()

    # =====================================================
    # RUN DIJKSTRA
    # =====================================================

    distances, previous = dijkstra(graph, source)

    end_time = time.time()

    # =====================================================
    # CHECK ROUTE EXISTENCE
    # =====================================================

    if distances[destination] == float('inf'):

        print("\nNo Route Exists!")

        exit()

    # =====================================================
    # SHORTEST PATH
    # =====================================================

    path = get_path(previous, destination)

    # =====================================================
    # OUTPUT
    # =====================================================

    print("\n================================================")
    print("           OPTIMAL ROUTE RESULT")
    print("================================================")

    print("\nSource Location      :", source)

    print("Destination Location :", destination)

    print(
        "\nShortest Distance    :",
        distances[destination],
        "km"
    )

    print("\nOptimal Route        :")

    print("\n   " + "  →  ".join(path))

    # =====================================================
    # ESTIMATED TIME
    # =====================================================

    estimated_time = distances[destination] * 3

    print(
        "\nEstimated Travel Time:",
        estimated_time,
        "minutes"
    )

    # =====================================================
    # FUEL COST
    # =====================================================

    fuel_cost = distances[destination] * 5

    print(
        "\nEstimated Fuel Cost  : ₹",
        fuel_cost
    )

    # =====================================================
    # EXECUTION TIME
    # =====================================================

   # execution_time = end_time - start_time

   # print(
    #    "\nExecution Time       :",
      #  execution_time,
      #  "seconds"
    #)

    # =====================================================
    # TRAFFIC ANALYSIS
    # =====================================================

    print("\n================================================")
    print("             TRAFFIC ANALYSIS")
    print("================================================")

    for i in range(len(path)-1):

        edge = (path[i], path[i+1])

        if edge in traffic:

            print(
                "\n",
                edge[0],
                "→",
                edge[1],
                ":",
                traffic[edge]
            )

    # =====================================================
    # ALL POSSIBLE ROUTES
    # =====================================================

    print("\n================================================")
    print("            ALL POSSIBLE ROUTES")
    print("================================================")

    routes = find_all_routes(
        graph,
        source,
        destination
    )

    route_data = []

    for route in routes:

        distance = calculate_distance(route)

        route_data.append((distance, route))

    route_data.sort()

    rank = 1

    for distance, route in route_data:

        print(
            "\nRoute",
            rank,
            ":",
            " → ".join(route)
        )

        print("Distance :", distance, "km")

        rank += 1

    # =====================================================
    # GRAPH VISUALIZATION
    # =====================================================

    G = nx.DiGraph()

    # ADD EDGES

    for node in graph:

        for neighbor, weight in graph[node]:

            G.add_edge(node, neighbor, weight=weight)

    # POSITION

    pos = nx.spring_layout(G, seed=42)

    # NODE COLORS

    node_colors = []

    for node in G.nodes():

        if node == source:

            node_colors.append('green')

        elif node == destination:

            node_colors.append('orange')

        elif node in path:

            node_colors.append('red')

        else:

            node_colors.append('skyblue')

    # DRAW GRAPH

    plt.figure(figsize=(12, 8))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=3500,
        font_size=10,
        font_weight='bold',
        arrows=True
    )

    # EDGE LABELS

    labels = nx.get_edge_attributes(
        G,
        'weight'
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels,
        font_size=9
    )

    # HIGHLIGHT SHORTEST PATH

    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        edge_color='red',
        width=4,
        arrows=True
    )

    # TITLE

    plt.title(
        "DYNAMIC TRAFFIC-AWARE SMART ROUTE OPTIMIZER",
        fontsize=14,
        fontweight='bold'
    )

    plt.show()

# =========================================================
# END OF PROJECT
# =========================================================