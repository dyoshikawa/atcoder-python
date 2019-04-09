def gen_graph(input_list):
    graph = {}

    for item in input_list:
        if not item[0] in graph:
            graph[item[0]] = {}
        graph[item[0]][item[1]] = item[2]

    return graph


def get_lowest_cost_vertex(costs):

    return ""


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

    print(costs)
    print(parents)
    # get_lowest_cost_vertex(costs)

    return ""


def main(vertex_count, input_list):
    print(input_list)
    graph = gen_graph(input_list)
    print(graph)

    for start in range(1, vertex_count+1):
        for goal in range(1, vertex_count+1):
            route = get_best_route(graph, start, goal)
            print(route)

    return input_list[0][0]


if __name__ == "__main__":
    vertex_count, sides_count = list(map(int, input().split()))
    input_list = []
    for _ in sides_count:
        vertex_1, vertex_2, distance = list(map(int, input().split()))
        input_list.append((vertex_1, vertex_2, distance))
    print(main(vertex_count, input_list))
