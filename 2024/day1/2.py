def similarity_score(list, number):
    sum = 0

    for i in list:
        if i == number:
            sum += 1
    
    return sum * number

def main():
    first_column = []
    second_column = []

    sum = 0

    with open("example1_2.txt", "r") as w:
        for i in w:
            i = i.replace("\n", "")
            line = i.split(" ")

            first_column.append(int(line[0]))
            second_column.append(int(line[len(line)-1]))

    length = len(first_column)
    i = 0
    while i < length:
        sum += similarity_score(second_column, first_column[i])
        i += 1
    print(sum)


if __name__ == "__main__":
    main()
