def read_input(file: str):
    with open(file, "r") as f:
        contents = f.read()

    lines = contents.split("\n")
    map(lambda line: line.strip(), lines)
    lines = lines[:-1]

    return lines


def part1(input: list[str]):
    sum_joltage = 0

    for line in input:
        nums = list(line)

        current_max = 0
        for idx, num in enumerate(nums):
            for s in range(idx + 1, len(nums)):
                current = int(f"{num}{nums[s]}")
                if current > current_max:
                    current_max = current

        sum_joltage += current_max

    print(sum_joltage)


def part2(input: list[str]):
    pass


if __name__ == "__main__":
    file = str("input")
    data = read_input(file)

    part1(data)
    part2(data)
