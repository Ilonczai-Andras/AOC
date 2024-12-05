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


def main():
    file_path = "example1_1.txt"
    rules, updates = parse_rules_and_updates(file_path)

    middle_pages = []

    for update in updates:
        if validate_update(rules, update):
            middle_pages.append(update[len(update) // 2])

    result = sum(middle_pages)

    print(f"Sum of middle pages: {result}")


if __name__ == "__main__":
    main()
