from math import ceil


def main(N, Q, S, lr_list):
    res = []
    for lr in lr_list:
        l, r = lr
        res.append(S[l-1:r].count("AC"))
    return res


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    S = input()
    lr_list = []
    for _ in range(Q):
        lr_list.append(tuple(map(int, input().split())))
    res = main(N, Q, S, lr_list)
    for r in res:
        print(r)
