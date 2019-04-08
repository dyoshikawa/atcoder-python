import itertools


def main(input_list):
    tuple_list = []
    for item in input_list:
        splitted = list(map(int, item.split()))
        tuple_list.append((splitted[0], splitted[1]))

    combination_list = list(itertools.combinations(tuple_list, 2))

    result_list = []
    for item in combination_list:
        result = ((item[0][0] - item[1][0]) ** 2 +
                  (item[0][1] - item[1][1]) ** 2) ** 0.5
        result_list.append(result)

    return max(result_list)


if __name__ == "__main__":
    input_1 = int(input())
    input_list = []
    for _ in range(input_1):
        input_list.append(input())
    print(main(input_list))
