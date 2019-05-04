def main(word):
    strs = list(word)
    reversed_strs = list(reversed(strs))

    last_del_num = 0
    for i, s in enumerate(reversed_strs):
        if s == ".":
            break
        if s == "#":
            last_del_num += 1

    del(reversed_strs[0:last_del_num])

    b_count = reversed_strs.count("#")
    w_count = reversed_strs.count(".")

    if b_count == 0:
        return 0

    if w_count == 0:
        return 0

    if b_count < w_count:
        return b_count

    return w_count


if __name__ == "__main__":
    input()
    word = input()
    print(main(word))
