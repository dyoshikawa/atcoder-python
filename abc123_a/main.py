import copy


def main(input_nums):
    k = input_nums[5]
    nums = copy.deepcopy(input_nums)
    nums.pop(5)

    for i_a, num_a in enumerate(nums):
        for i_b, num_b in enumerate(nums):
            if i_a != i_b:
                if abs(num_a - num_b) > k:
                    return ":("

    return "Yay!"


if __name__ == "__main__":
    input_nums = []
    for _ in range(6):
        input_nums.append(int(input()))
    print(main(input_nums))
