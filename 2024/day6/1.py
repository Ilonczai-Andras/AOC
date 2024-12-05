def stringToArray(line: str) -> list[str]:
    result = []
    for i in line:
        result.append(i)
    return result


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("")
    print("-" * 20)


def whereIsGuard(matrix: list[str]):
    guards = ["^", "v", ">", "<"]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in guards:
                return i, j, matrix[i][j]
    return None, None, None


def isGuardOut(matrix: list[str], h, w):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1

    if h is None or w is None:
        return True

    if h > height or h < 0:
        return True
    if w > width or w < 0:
        return True
    return False


def move(matrix: list[str], i: int, j: int, direction: str, visited: set):
    if direction == "up":
        starti, startj = i, j
        endi = 0
        while i >= 0 and matrix[i][j] != "#":
            endi = i
            visited.add((i, j))
            i -= 1
        matrix[endi][startj] = ">"
        matrix[starti][startj] = "."

    if direction == "right":
        starti, startj = i, j
        endj = 0
        while j < len(matrix[0]) and matrix[i][j] != "#":
            endj = j
            visited.add((i, j))
            j += 1
        matrix[starti][endj] = "v"
        matrix[starti][startj] = "."

    if direction == "down":
        starti, startj = i, j
        endi = 0
        while i < len(matrix) and matrix[i][j] != "#":
            endi = i
            visited.add((i, j))
            i += 1
        matrix[endi][startj] = "<"
        matrix[starti][startj] = "."

    if direction == "left":
        starti, startj = i, j
        endj = 0
        while j >= 0 and matrix[i][j] != "#":
            endj = j
            visited.add((i, j))
            j -= 1
        matrix[starti][endj] = "^"
        matrix[starti][startj] = "."


def main():
    matrix: list[str] = []
    visited = set()
    file_path = "example.txt"

    with open(file_path, "r") as w:
        for i in w:
            i = i.replace("\n", "")
            matrix.append(stringToArray(i))

    printMatrix(matrix)
    i, j, type = whereIsGuard(matrix)

    if i is not None and j is not None:
        visited.add((i, j))

    while not isGuardOut(matrix, i, j):
        if type == "^":
            # print("UP")
            move(matrix, i, j, "up", visited)
            printMatrix(matrix)
        elif type == "v":
            # print("DOWN")
            move(matrix, i, j, "down", visited)
            printMatrix(matrix)
        elif type == "<":
            # print("LEFT")
            move(matrix, i, j, "left", visited)
            printMatrix(matrix)
        elif type == ">":
            # print("RIGHT")
            move(matrix, i, j, "right", visited)
            printMatrix(matrix)

        i, j, type = whereIsGuard(matrix)

    print(f"The guard will visit {len(visited)} distinct positions on your map.")


if __name__ == "__main__":
    main()
