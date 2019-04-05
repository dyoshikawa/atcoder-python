def main(input):
    input_nums = list(map(int, input[1].split(" ")))
    count = 0
    while True:
        exist_odd = False
        for num in input_nums:
            if num % 2 != 0:
                exist_odd = True
        if exist_odd:
            break
        input_nums = list(map(lambda x: x / 2, input_nums))
        count += 1
    return count


if __name__ == "__main__":
    input_1 = input()
    input_2 = input()
    print(main([input_1, input_2]))
