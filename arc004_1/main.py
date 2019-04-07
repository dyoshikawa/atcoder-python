from collections import deque


def filter_space_list(strs):
    space_list = []
    x = 1
    for str in strs:
        y = 1
        for char in str:
            if char == ".":
                space_list.append((x, y))
            y += 1
        x += 1
    return space_list


def create_graph(strs):
    space_list = filter_space_list(strs)
    graph = {}
    for space in space_list:
        graph[space] = [
            x for x in [
                (space[0]+1, space[1]),
                (space[0], space[1]+1),
                (space[0]-1, space[1]),
                (space[0], space[1]-1),
            ] if x in space_list
        ]
    print(graph)
    return graph


def main(input_list):
    s_list = list(map(int, input_list[0][1].split()))
    sy = s_list[0]
    sx = s_list[1]
    g_list = list(map(int, input_list[0][2].split()))
    gy = g_list[0]
    gx = g_list[1]
    create_graph(input_list[1])


if __name__ == "__main__":
    input_nums = []
    for _ in range(5):
        input_nums.append(int(input()))
    print(main(input_nums))
