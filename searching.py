import json

def read_data(filename, field):
    with open("sequential.json", "r") as file:
        lines = json.load(file)

    if field not in lines:
        return None

    with open(filename, "r") as file:
        data = json.load(file)

    return data.get(field, None)

def main():
    data1 = read_data("sequential.json", "unordered_numbers")
    print(data1)

if __name__ == "__main__":
    main()