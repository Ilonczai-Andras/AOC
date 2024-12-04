def stringToArray(line: str) -> list[str]:
    result = []

    for i in line:
        result.append(i)
    return result


def containNeg(list: list[int]) -> bool:
    return any(True for i in list if i < 0)


def xmasPartOne(matrix: list[str], i: int, j: int):
    try:
        indexes = [i + 1, i - 1, j - 1, j + 1]
        if containNeg(indexes):
            raise IndexError
        return matrix[i + 1][j - 1] + matrix[i][j] + matrix[i - 1][j + 1]
    except IndexError:
        return ""


def xmasPartTwo(matrix: list[str], i: int, j: int):
    try:
        indexes = [i - 1, i + 1, j - 1, j + 1]
        if containNeg(indexes):
            raise IndexError
        return matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
    except IndexError:
        return ""


def XMas(matrix: list[str], i: int, j: int):
    patterns = ["MAS", "SAM"]
    return (
        xmasPartOne(matrix, i, j) in patterns and xmasPartTwo(matrix, i, j) in patterns
    )


def main():
    matrix: list[str] = []
    count = 0

    with open("example1_2.txt", "r") as w:
        for i in w:
            i = i.replace("\n", "")
            matrix.append(stringToArray(i))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if XMas(matrix, i, j):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
