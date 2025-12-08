def read_input(file: str):
    with open(file, "r") as f:
        contents = f.read()

    contents = contents.strip()
    return contents


def part1(input: str):
    lines: list[str] = input.splitlines()
    grid: list[list[str]] = list(map(lambda line: list(line), lines))

    s_index = grid[0].index("S")
    grid[1][s_index] = "|"

    active_beams: list[int] = [s_index]
    total_times_split: int = 0

    current_row = 1
    max_rows = len(grid)

    while current_row < max_rows:
        next_beams: list[int] = []

        if current_row + 1 >= max_rows:
            break

        for col_index in active_beams:
            cell_below = grid[current_row + 1][col_index]

            if cell_below == "^":
                total_times_split += 1

                left_col = col_index - 1
                if left_col >= 0:
                    next_beams.append(left_col)
                    # grid[current_row + 1][left_col] = "|"

                right_col = col_index + 1
                if right_col <= len(grid[current_row]):
                    next_beams.append(right_col)
                    # grid[current_row + 1][right_col] = "|"
            else:
                next_beams.append(col_index)
                # grid[current_row + 1][col_index] = "|"

        active_beams = sorted(set(next_beams))
        current_row += 1

    # for line in grid:
    #     for char in line:
    #         print(char, end=" ")
    #     print()

    print(total_times_split)


if __name__ == "__main__":
    file = "input"
    input = read_input(file)

    part1(input)
