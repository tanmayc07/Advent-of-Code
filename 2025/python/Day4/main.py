def read_input(file: str):
    with open(file, "r") as f:
        contents = f.read()

    contents = contents.strip()
    return contents


def convert_input(contents: str) -> list[list[str]]:
    mat = []
    outer = contents.splitlines()
    for lines in outer:
        mat.append(list(lines))

    return mat


def check_neighbours(matrix: list[list[str]], lidx: int, idx: int):
    count = 0
    count += (
        1 if lidx - 1 >= 0 and idx - 1 >= 0 and matrix[lidx - 1][idx - 1] == "@" else 0
    )
    count += 1 if lidx - 1 >= 0 and matrix[lidx - 1][idx] == "@" else 0
    count += (
        1
        if lidx - 1 >= 0
        and idx + 1 < len(matrix[lidx])
        and matrix[lidx - 1][idx + 1] == "@"
        else 0
    )
    count += 1 if idx - 1 >= 0 and matrix[lidx][idx - 1] == "@" else 0
    count += 1 if idx + 1 < len(matrix[lidx]) and matrix[lidx][idx + 1] == "@" else 0
    count += (
        1
        if lidx + 1 < len(matrix) and idx - 1 >= 0 and matrix[lidx + 1][idx - 1] == "@"
        else 0
    )
    count += 1 if lidx + 1 < len(matrix) and matrix[lidx + 1][idx] == "@" else 0
    count += (
        1
        if lidx + 1 < len(matrix)
        and idx + 1 < len(matrix[lidx])
        and matrix[lidx + 1][idx + 1] == "@"
        else 0
    )
    return count < 4


def part1(matrix: list[list[str]]):
    num_accessible_rolls = 0
    for lidx, line in enumerate(matrix):
        for idx, char in enumerate(line):
            if char == "@" and check_neighbours(matrix, lidx, idx):
                num_accessible_rolls += 1
    print(num_accessible_rolls)


def check_neighbours2(matrix: list[list[str]], lidx: int, idx: int):
    count = 0
    count += (
        1
        if lidx - 1 >= 0
        and idx - 1 >= 0
        and (matrix[lidx - 1][idx - 1] == "@" or matrix[lidx - 1][idx - 1] == "X")
        else 0
    )
    count += (
        1
        if lidx - 1 >= 0
        and (matrix[lidx - 1][idx] == "@" or matrix[lidx - 1][idx] == "X")
        else 0
    )
    count += (
        1
        if lidx - 1 >= 0
        and idx + 1 < len(matrix[lidx])
        and (matrix[lidx - 1][idx + 1] == "@" or matrix[lidx - 1][idx + 1] == "X")
        else 0
    )
    count += (
        1
        if idx - 1 >= 0
        and (matrix[lidx][idx - 1] == "@" or matrix[lidx][idx - 1] == "X")
        else 0
    )
    count += (
        1
        if idx + 1 < len(matrix[lidx])
        and (matrix[lidx][idx + 1] == "@" or matrix[lidx][idx + 1] == "X")
        else 0
    )
    count += (
        1
        if lidx + 1 < len(matrix)
        and idx - 1 >= 0
        and (matrix[lidx + 1][idx - 1] == "@" or matrix[lidx + 1][idx - 1] == "X")
        else 0
    )
    count += (
        1
        if lidx + 1 < len(matrix)
        and (matrix[lidx + 1][idx] == "@" or matrix[lidx + 1][idx] == "X")
        else 0
    )
    count += (
        1
        if lidx + 1 < len(matrix)
        and idx + 1 < len(matrix[lidx])
        and (matrix[lidx + 1][idx + 1] == "@" or matrix[lidx + 1][idx + 1] == "X")
        else 0
    )
    return count < 4


def part2(matrix: list[list[str]]):
    fl = True
    num_removable = 0
    while fl:
        num_accessible_rolls = 0
        for lidx, line in enumerate(matrix):
            for idx, char in enumerate(line):
                if char == "@" and check_neighbours2(matrix, lidx, idx):
                    num_accessible_rolls += 1
                    matrix[lidx][idx] = "X"

        for lidx, line in enumerate(matrix):
            for idx, char in enumerate(line):
                if char == "X":
                    matrix[lidx][idx] = "."

        num_removable += num_accessible_rolls
        if num_accessible_rolls == 0:
            fl = False

    print(num_removable)


if __name__ == "__main__":
    file = "input"
    input = read_input(file)
    matrix = convert_input(input)

    part1(matrix)
    part2(matrix)
