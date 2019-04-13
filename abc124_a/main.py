def main(a, b):
    return max([a+a-1,
                a+b,
                b+b-1,
                b+a])


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(main(a, b))
