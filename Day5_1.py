from collections import defaultdict

def load_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def parse_input(lines):
    rules = []
    updates = []
    is_update_section = False
    
    for line in lines:
        if not line:
            is_update_section = True
        elif is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
    
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph

def is_valid_order(update, graph):
    index_map = {page: idx for idx, page in enumerate(update)}
    
    for x, y in graph.items():
        if x in index_map:
            for y_page in y:
                if y_page in index_map and index_map[x] > index_map[y_page]:
                    return False
    return True

def find_middle_page(ordered_updates):
    middle_pages = []
    for update in ordered_updates:
        middle_page = update[len(update) // 2]
        middle_pages.append(middle_page)
    return sum(middle_pages)

if __name__ == "__main__":
    # Path to the input file
    file_path = 'day5.txt'
    
    # Load and parse the input
    lines = load_input(file_path)
    rules, updates = parse_input(lines)
    
    # Build the dependency graph from rules
    graph = build_graph(rules)
    
    # Find updates that are in the correct order
    ordered_updates = [update for update in updates if is_valid_order(update, graph)]
    
    # Find and sum the middle page numbers of the correctly ordered updates
    result = find_middle_page(ordered_updates)
    
    print(f"The sum of the middle page numbers from correctly ordered updates is: {result}")