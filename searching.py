import json


def read_data(filename, field):
    with open("sequential.json", "r") as file:
        lines = json.load(file)

    if field not in lines:
        return None

    with open(filename, "r") as file:
        data = json.load(file)

    return data.get(field, None)

def linear_search(sequence, number):
    slovnik = {}
    count = 0
    seznam = []
    for idx, value in enumerate(sequence):
        if value == number:
            seznam.append(idx)
            count += 1
    slovnik["positions"] = seznam
    slovnik["count"] = count
    return slovnik

def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        middle = (right + left) // 2
        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return None


def main():
    data1 = read_data("sequential.json", "ordered_numbers")
    print(data1)
    number = 7
    result = linear_search(data1, number)
    print(result)
    binar = binary_search(data1, number)
    print(binar)

if __name__ == "__main__":
    main()