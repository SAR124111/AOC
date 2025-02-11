def read_input(file_path):
    list1 = []
    list2 = []
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2

def reconcile_lists(list1, list2):
    # Step 1: Sort both lists
    list1.sort()
    list2.sort()
    
    # Step 2: Pair up numbers and calculate distances
    total_distance = 0
    for num1, num2 in zip(list1, list2):
        total_distance += abs(num1 - num2)
    
    return total_distance

def main():
    file_path = 'Day1.txt'  # Replace with your actual file path
    list1, list2 = read_input(file_path)
    result = reconcile_lists(list1, list2)
    print(f"Total distance: {result}")

if __name__ == '__main__':
    main()
