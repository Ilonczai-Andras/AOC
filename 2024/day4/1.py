def stringToArray(line: str) -> list[str]:
    result = []

    for i in line:
        result.append(i)
    return result


def containNeg(list: list[int]) -> bool:
    return any(True for i in list if i < 0)


def toNorth(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [i - 1, i - 2, i - 3]

        if containNeg(indexes):
            raise IndexError

        return matrix[i][j] + matrix[i - 1][j] + matrix[i - 2][j] + matrix[i - 3][j]
    except IndexError:
        return None


def toNorthEast(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = indexes = [i - 1, i - 2, i - 3, j + 1, j + 2, j + 3]

        if containNeg(indexes):
            raise IndexError

        return (
            matrix[i][j]
            + matrix[i - 1][j + 1]
            + matrix[i - 2][j + 2]
            + matrix[i - 3][j + 3]
        )
    except IndexError:
        return None


def toEast(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [j + 1, j + 2, j + 3]

        if containNeg(indexes):
            raise IndexError

        return matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i][j + 3]
    except IndexError:
        return None


def toSouthEast(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [i + 1, i + 2, i + 3, j + 1, j + 2, j + 3]

        if containNeg(indexes):
            raise IndexError
        return (
            matrix[i][j]
            + matrix[i + 1][j + 1]
            + matrix[i + 2][j + 2]
            + matrix[i + 3][j + 3]
        )
    except IndexError:
        return None


def toSouth(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [i + 1, i + 2, i + 3]

        if containNeg(indexes):
            raise IndexError

        return matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j]
    except IndexError:
        return None


def toSouthWest(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [j - 1, j - 2, j - 3]

        if containNeg(indexes):
            raise IndexError

        return (
            matrix[i][j]
            + matrix[i + 1][j - 1]
            + matrix[i + 2][j - 2]
            + matrix[i + 3][j - 3]
        )
    except IndexError:
        return None


def toWest(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [j - 1, j - 2, j - 3]

        if containNeg(indexes):
            raise IndexError

        return matrix[i][j] + matrix[i][j - 1] + matrix[i][j - 2] + matrix[i][j - 3]
    except IndexError:
        return None


def toNorthWest(matrix: list[str], i: int, j: int) -> str:
    try:
        indexes = [i - 1, i - 2, i - 3, j - 1, j - 2, j - 3]

        if containNeg(indexes):
            raise IndexError

        return (
            matrix[i][j]
            + matrix[i - 1][j - 1]
            + matrix[i - 2][j - 2]
            + matrix[i - 3][j - 3]
        )
    except IndexError:
        return None


def appendWords(matrix: list[str], i: int, j: int) -> list[str]:
    result: list[str] = []
    result.append(toEast(matrix, i, j))
    result.append(toSouthEast(matrix, i, j))
    result.append(toSouth(matrix, i, j))
    result.append(toSouthWest(matrix, i, j))
    result.append(toWest(matrix, i, j))
    result.append(toNorthWest(matrix, i, j))
    result.append(toNorth(matrix, i, j))
    result.append(toNorthEast(matrix, i, j))

    return [word for word in result if word is not None]


def main():
    matrix: list[str] = []
    count = 0

    with open("example1_1.txt", "r") as w:
        for i in w:
            i = i.replace("\n", "")
            matrix.append(stringToArray(i))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            words: list[str] = appendWords(matrix, i, j)

            count += sum([1 for w in words if w == "XMAS"])
    print(count)


if __name__ == "__main__":
    main()
