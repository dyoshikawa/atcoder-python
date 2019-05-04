def main(num_1, num_2, num_3):
    if (num_3 > num_1 and num_3 > num_2) or (num_3 < num_1 and num_3 < num_2):
        return 'No'
    else:
        return 'Yes'


if __name__ == "__main__":
    num_1, num_2, num_3 = list(map(int, input().split()))
    print(main(num_1, num_2, num_3))
