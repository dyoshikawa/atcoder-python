import copy


def isNumsDouble(nums):
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False


def main(input_nums):
    total_list = []
    for i_a, num_a in enumerate(input_nums):
        for i_b, num_b in enumerate(input_nums):
            for i_c, num_c in enumerate(input_nums):
                for i_d, num_d in enumerate(input_nums):
                    for i_e, num_e in enumerate(input_nums):
                        if isNumsDouble([i_a, i_b, i_c, i_d, i_e]):
                            continue
                        total = 0
                        for num in [num_a, num_b, num_c, num_d, num_e]:
                            rem = total % 10
                            if rem != 0:
                                total += 10 - rem
                            total += num
                        total_list.append(total)
    return min(total_list)


if __name__ == "__main__":
    input_nums = []
    for _ in range(5):
        input_nums.append(int(input()))
    print(main(input_nums))
