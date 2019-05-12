def main(N, K, a_list):
    s_list = [0]
    for i, _ in enumerate(a_list):
        s_list.append(s_list[i] + a_list[i])

    res = float('-inf')
    for i in range(N-K):
        val = s_list[K+i] - s_list[i]
        if val > res:
            res = val

    return res
