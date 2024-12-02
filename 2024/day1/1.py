def main():
    first_column = []
    second_column = []

    sum = 0

    with open("example1_1.txt", "r") as w:
        for i in w:
            i = i.replace("\n", "")
            line = i.split(" ")

            first_column.append(int(line[0]))
            second_column.append(int(line[len(line)-1]))
    first_column.sort()
    second_column.sort()

    length = len(first_column)
    i = 0
    while i < length:
        sum = sum + abs(first_column[i] - second_column[i])
        i += 1
    print(sum)


if __name__ == "__main__":
    main()
