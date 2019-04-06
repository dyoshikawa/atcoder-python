def main(input_nums):
    count = 0
    for a in range(0, input_nums[0]+1):
        for b in range(0, input_nums[1]+1):
            for c in range(0, input_nums[2]+1):
                if (500 * a + 100 * b + 50 * c) == input_nums[3]:
                    count += 1
    return count


if __name__ == "__main__":
    input_1 = int(input())
    input_2 = int(input())
    input_3 = int(input())
    input_4 = int(input())
    print(main([input_1, input_2, input_3, input_4]))
