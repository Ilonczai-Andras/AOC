def parse_rules_and_updates(file_path):
    rules = []
    updates = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                x, y = map(int, line.split("|"))
                rules.append((x, y))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))

    return rules, updates


def validate_update(rules, update):
    page_index = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] > page_index[y]:
                return False
    return True


def reorder_update(rules, update):
    def compare_pages(a, b):
        for x, y in rules:
            if a == x and b == y:
                return -1
            if a == y and b == x:
                return 1
        return 0

    from functools import cmp_to_key

    return sorted(update, key=cmp_to_key(compare_pages))


def main():
    file_path = "example1_2.txt"
    rules, updates = parse_rules_and_updates(file_path)

    incorrectly_ordered = []
    for update in updates:
        if not validate_update(rules, update):
            incorrectly_ordered.append(update)

    reordered_middle_pages = []
    for update in incorrectly_ordered:
        reordered = reorder_update(rules, update)
        reordered_middle_pages.append(reordered[len(reordered) // 2])

    result = sum(reordered_middle_pages)
    print(f"Sum of middle pages for reordered updates: {result}")


if __name__ == "__main__":
    main()
