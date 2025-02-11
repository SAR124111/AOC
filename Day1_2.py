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
    
    # Step 2: Count Entries in list 2
    count_of_number = {}
    for num2 in list2:
        if num2 in count_of_number:
            count_of_number[num2] += 1
        else:
            count_of_number[num2] = 1
    
    # Calculate the similarity score
    similarity_score = 0
    for num in list1:
        if num in count_of_number:
            similarity_score += num * count_of_number[num]
    
    return similarity_score


            

def main():
    file_path = 'Day1.txt'  # Replace with your actual file path
    list1, list2 = read_input(file_path)
    result = reconcile_lists(list1, list2)
    print(f"Total distance: {result}")

if __name__ == '__main__':
    main()
