def main(input):
    inputStrs = list(input)
    sum = 0
    for str in inputStrs:
        if str == "1":
            sum += 1
    return sum


if __name__ == "__main__":
    print(main(input()))
