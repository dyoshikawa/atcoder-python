def gen_graph(input_list):
    graph = {}

    for item in input_list:
        if not item[0] in graph:
            graph[item[0]] = {}
        if not item[1] in graph:
            graph[item[1]] = {}
        graph[item[0]][item[1]] = item[2]
        graph[item[1]][item[0]] = item[2]

    return graph


def get_lowest_cost_vertex(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def get_best_routes(graph, start):
    costs = {}
    parents = {}
    processed = []

    costs[start] = 0
    parents[start] = None
    processed.append(start)

    for item in graph[start].keys():
        costs[item] = graph[start][item]
        parents[item] = start

    for item in graph.keys():
        if not (item in costs.keys() or item == start):
            costs[item] = float("inf")
            parents[item] = None

    node = get_lowest_cost_vertex(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = get_lowest_cost_vertex(costs, processed)

    routes = []
    for item in graph.keys():
        if item != start:
            route = []
            route.append(item)
            parent = parents[item]
            while 1:
                route.append(parent)
                if parent == start:
                    break
                parent = parents[parent]
            route.reverse()
            routes.append(route)
    return routes


def main(vertex_count, input_list):
    graph = gen_graph(input_list)

    routes = []
    for start in range(1, vertex_count+1):
        for route in get_best_routes(graph, start):
            routes.append(route)

    route_strs = []
    for route in routes:
        route_strs.append(''.join(list(map(str, route))))

    side_strs = []
    for item in input_list:
        side_strs.append(str(item[0]) + str(item[1]))
        # side_strs.append(str(item[1]) + str(item[0]))

    count = 0
    route_strs_joined = '/'.join(route_strs)

    for side_str in side_strs:
        if route_strs_joined.find(side_str) == -1:
            count += 1

    return count


if __name__ == "__main__":
    input_1 = input()
    vertex_count, sides_count = list(map(int, input_1.split()))
    input_list = []
    for _ in range(sides_count):
        vertex_1, vertex_2, distance = list(map(int, input().split()))
        input_list.append((vertex_1, vertex_2, distance))
    print(main(vertex_count, input_list))
