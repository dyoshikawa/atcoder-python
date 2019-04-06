def main(input_list):
    input_temperatures = list(map(int, input_list[0].split(" ")))
    input_height_list = [{'value': x, 'key': i+1}
                         for i, x in enumerate(list(map(int, input_list[1].split(" "))))]

    temperatures = list(
        map(lambda x: {'key': x['key'], 'value': input_temperatures[0] - x['value'] * 0.006}, input_height_list))
    diff_list = list(
        map(lambda x: {'key': x['key'], 'value': abs(input_temperatures[1] - x['value'])}, temperatures))
    diff_list_sorted = sorted(diff_list, key=lambda x: x['value'])

    return diff_list_sorted[0]['key']


if __name__ == "__main__":
    input()
    input_2 = input()
    input_3 = input()
    print(main([input_2, input_3]))
