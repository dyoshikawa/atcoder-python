from math import ceil


def main(N, A, B, C, D, E):
    loads = [A, B, C, D, E]
    min_val = min(loads)
    min_index = loads.index(min_val)

    res = min_index + ceil(N / min_val) + (5 - (min_index + 1))

    return res


if __name__ == "__main__":
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(main(N, A, B, C, D, E))
