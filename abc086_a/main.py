def main(input):
    inputNums = list(map(int, input.split(" ")))
    prod = inputNums[0] * inputNums[1]
    if prod % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    print(main(input()))
