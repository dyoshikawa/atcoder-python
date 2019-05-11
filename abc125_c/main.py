from fractions import gcd


def main(input_1, input_2):
    left = [0] * (input_1+1)
    for i in range(input_1):
        left[i+1] = gcd(left[i], input_2[i])

    right = [0] * (input_1 + 1)
    i = input_1 - 1
    while i >= 0:
        right[i] = gcd(right[i+1], input_2[i])
        i -= 1

    while i >= 0:
        right[i] = gcd(right[i+1], input_2[i])

    res = 0
    for i in range(input_1):
        l = left[i]
        r = right[i+1]
        gcd_val = gcd(l, r)
        if gcd_val > res:
            res = gcd_val

    return res


if __name__ == "__main__":
    input_1 = int(input())
    input_2 = list(map(int, input().split()))
    print(main(input_1, input_2))
