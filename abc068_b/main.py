def main(input):
    input_num = int(input)
    max_count = 0
    max_num = 1
    for i in range(1, input_num + 1):
        count = 0
        divided = i
        while True:
            if divided % 2 != 0:
                break
            divided = divided / 2
            count += 1
            if count > max_count:
                max_count = count
                max_num = i

    return max_num


if __name__ == "__main__":
    input_1 = input()
    print(main(input_1))
