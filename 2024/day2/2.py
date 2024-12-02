def isDecreasing(list):
    for i in range(0, len(list) - 1):
        if not int(list[i]) > int(list[i + 1]):
            return False
    return True


def isIncreasing(list):
    for i in range(0, len(list) - 1):
        if not int(list[i]) < int(list[i + 1]):
            return False
    return True


def isSave(line):
    line = line.split(" ")
    isDecr = isDecreasing(line)
    isIncr = isIncreasing(line)

    if isDecr == False and isIncr == False:
        return False

    for i in range(0, len(line) - 1):
        first = abs(int(line[i]) - int(line[i + 1]))

        if first not in [1, 2, 3]:
            return False
    return True


def Problem_Dampener(list):
    original = isSave(list)
    if original:
        return True

    list = list.split(" ")
    length = len(list)
    isSaveNow = False
    cnt = 0

    for i in range(0, len(list)):
        copy = list.copy()
        copy.pop(i)
        isSaveNow = isSave(" ".join(copy))
        if isSaveNow:
            return True
        cnt += 1 if isSaveNow == False else 0
    return cnt != length


def main():

    sum = 0

    with open("example1_2.txt", "r") as w:
        for i in w:
            i = i.replace("\n", "")
            sum += 1 if Problem_Dampener(i) == True else 0
    print(sum)


if __name__ == "__main__":
    main()
