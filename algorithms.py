import heapq
import math
import time

def euclidean(a, b):
    return math.sqrt((a["x"] - b["x"])**2 + (a["y"] - b["y"])**2 + ((a.get("z", 0)-b.get("z", 0))*1.8)**2)

def build_adjacency(graph, accessible=False):
    adjacency = {node_id: [] for node_id in graph["nodes"]}
    for edge in graph["edges"]:
        if accessible and not edge.get("accessible", False):
            continue
        a, b = edge["from"], edge["to"]
        weight = float(edge.get("weight", euclidean(graph["nodes"][a], graph["nodes"][b])))
        adjacency[a].append((b, weight))
        adjacency[b].append((a, weight))
    return adjacency

def reconstruct_path(previous, start, goal):
    if goal not in previous and goal != start:
        return []
    path, current = [goal], goal
    while current != start:
        current = previous.get(current)
        if current is None:
            return []
        path.append(current)
    return list(reversed(path))

def find_route(graph, start, goal, algorithm="dijkstra", accessible=False):
    nodes = graph["nodes"]
    adjacency = build_adjacency(graph, accessible)
    started = time.perf_counter()
    distances = {node: float("inf") for node in nodes}
    distances[start] = 0.0
    previous = {}
    visited_order = []
    closed = set()

    def heuristic(node_id):
        return euclidean(nodes[node_id], nodes[goal])

    queue = [(heuristic(start) if algorithm == "astar" else 0.0, 0.0, start)]
    while queue:
        _, current_cost, current = heapq.heappop(queue)
        if current in closed:
            continue
        closed.add(current)
        visited_order.append(current)
        if current == goal:
            break
        for neighbor, weight in adjacency[current]:
            new_cost = current_cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current
                priority = new_cost + (heuristic(neighbor) if algorithm == "astar" else 0.0)
                heapq.heappush(queue, (priority, new_cost, neighbor))

    elapsed_ms = (time.perf_counter() - started) * 1000
    path = reconstruct_path(previous, start, goal)
    if not path:
        return {"path": [], "error": "unreachable"}

    route_nodes = [nodes[node_id] | {"id": node_id} for node_id in path]
    return {
        "algorithm": "A*" if algorithm == "astar" else "Dijkstra",
        "path": path,
        "route_nodes": route_nodes,
        "distance": round(distances[goal], 2),
        "visited_count": len(visited_order),
        "visited_order": visited_order,
        "execution_ms": round(elapsed_ms, 4),
        "accessible_only": accessible,
        "steps": [f"Start at {nodes[path[0]]['name']}"] +
                 [f"Continue to {nodes[n]['name']}" for n in path[1:-1]] +
                 [f"Arrive at {nodes[path[-1]]['name']}"]
    }
