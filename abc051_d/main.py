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


def get_best_route(graph, start, goal):
    costs = {}
    parents = {}

    for item in graph[start].keys():
        costs[item] = graph[start][item]
        parents[item] = start

    for item in graph.keys():
        if not (item in costs.keys() or item == start):
            costs[item] = float("inf")
            parents[item] = None

    # print(costs)
    # print(parents)
    processed = []
    print("start")
    print(start)

    node = get_lowest_cost_vertex(costs, processed)
    print("最も近いnode")
    print(node)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            print(costs)
            print(n)
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
            processed.append(node)
            node = get_lowest_cost_vertex(costs, processed)

    print(parents)
    return ""


def main(vertex_count, input_list):
    print(input_list)
    graph = gen_graph(input_list)
    print(graph)

    for start in range(1, vertex_count+1):
        for goal in range(1, vertex_count+1):
            route = get_best_route(graph, start, goal)
            # print(route)

    return input_list[0][0]


if __name__ == "__main__":
    vertex_count, sides_count = list(map(int, input().split()))
    input_list = []
    for _ in sides_count:
        vertex_1, vertex_2, distance = list(map(int, input().split()))
        input_list.append((vertex_1, vertex_2, distance))
    print(main(vertex_count, input_list))
