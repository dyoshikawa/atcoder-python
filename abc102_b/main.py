def main(input):
    input_nums = list(map(int, input.split(" ")))
    return max(input_nums) - min(input_nums)


if __name__ == "__main__":
    input()
    print(main(input()))
