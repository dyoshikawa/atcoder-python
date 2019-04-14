def main(input_str):
    input_list = list(input_str)
    count = 0
    if input_list[0] == "0":
        ans = []
        for i, _ in enumerate(input_list):
            if i % 2 == 0:
                ans.append("0")
            else:
                ans.append("1")
        for i, _ in enumerate(input_list):
            if input_list[i] != ans[i]:
                count += 1

    else:
        ans = []
        for i, _ in enumerate(input_list):
            if i % 2 == 0:
                ans.append("1")
            else:
                ans.append("0")
        for i, _ in enumerate(input_list):
            if input_list[i] != ans[i]:
                count += 1

    return count


if __name__ == "__main__":
    input_str = input()
    print(main(input_str))
