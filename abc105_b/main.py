def main(input_num):
    for a in range(input_num+1):
        for b in range(input_num+1):
            if (7 * a + 4 * b) == input_num:
                return "Yes"
    return "No"


if __name__ == "__main__":
    print(main(int(input())))
