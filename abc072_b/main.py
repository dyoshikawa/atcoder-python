def main(input_str):
    input_strs = list(input_str)
    strs_filtered = [x for i, x in enumerate(input_strs) if i % 2 == 0]
    return ''.join(strs_filtered)


if __name__ == "__main__":
    print(main(input()))
