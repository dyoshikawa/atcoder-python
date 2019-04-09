def main(n, a, b):
    target_list = []

    for i in range(1, n+1):
        nums = list(map(int, list(str(i))))
        total = sum(nums)
        if total >= a and total <= b:
            target_list.append(i)

    return sum(target_list)


if __name__ == "__main__":
    n, a, b = list(map(int, input().split()))
    print(main(n, a, b))
