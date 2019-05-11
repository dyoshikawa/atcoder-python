def main(N, K):
    return N - K + 1


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    print(main(N, K))
