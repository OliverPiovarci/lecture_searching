import json
import time
from generators import unordered_sequence, ordered_sequence
import matplotlib.pyplot as plt

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

def test_complexity():
    number = 42
    times_linear = []
    times_binear = []
    repetitions = 100
    list_of_n = [100, 500, 1000, 5000, 10000]
    for n in list_of_n:
        duration_linear = 0
        duration_binear = 0

        unordered_data = unordered_sequence(n)
        ordered_data = ordered_sequence(n)
        for _ in range(repetitions):
            start_time_linear = time.perf_counter()
            found_number = linear_search(unordered_data, number)
            end_time_linear = time.perf_counter()
            duration_linear += end_time_linear - start_time_linear

            start_time_binary = time.perf_counter()
            found_number_bin = binary_search(ordered_data, number)
            end_time_binary = time.perf_counter()
        times_linear.append(duration_linear / repetitions)
        times_binear.append(duration_binear / repetitions)
    return list_of_n, times_linear, times_binear

def main():
    data1 = read_data("sequential.json", "ordered_numbers")
    print(data1)
    number = 7
    repetitions = 100
    duration = 0
    for measurements in range(repetitions):
        start = time.perf_counter()
        result = linear_search(data1, number)
        end = time.perf_counter()
        duration += end - start

    print(result)
    print(duration / repetitions)
    binar = binary_search(data1, number)
    print(binar)
    sizes = [10, 20, 50, 100]
    test_complexity()

if __name__ == "__main__":
    main()