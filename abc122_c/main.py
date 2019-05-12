def main(N, Q, S, lr_list):
    chars = list(S)

    s_list = [0]
    for i in range(N):
        if i+1 < N and chars[i] == 'A' and chars[i+1] == 'C':
            s_list.append(s_list[i] + 1)
        else:
            s_list.append(s_list[i])

    res_list = []
    for lr in lr_list:
        l, r = lr
        l -= 1
        r -= 1
        res_list.append(s_list[r] - s_list[l])

    return res_list


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    S = input()
    lr_list = []
    for _ in range(Q):
        lr_list.append(tuple(map(int, input().split())))
    res = main(N, Q, S, lr_list)
    for r in res:
        print(r)
