import re


def read_input(file: str):
    with open(file, "r") as f:
        contents = f.read()

    lines = contents.split(",")
    return lines


# Simply loops over each ID between the interval and checks if both halves of the string are equal.
def part1(input: list[str]):
    sum_invalids = 0

    for current in input:
        (start, end) = current.split("-")
        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            i_as_str = str(i)
            mid = len(i_as_str) // 2
            if i_as_str[0:mid] == i_as_str[mid:]:
                sum_invalids += i

    print(sum_invalids)


# Uses Regex to match to the IDs defining the capturing group for one or more digits and using backreference for it.
def part2(input: list[str]):
    sum_invalids = 0

    for current in input:
        (start, end) = current.split("-")
        start = int(start)
        end = int(end)

        regex = r"^(\d+)\1+$"
        pat = re.compile(regex)
        for i in range(start, end + 1):
            i_as_str = str(i)
            if re.match(pat, i_as_str):
                sum_invalids += i

    print(sum_invalids)


if __name__ == "__main__":
    file = str("input")
    input = read_input(file)

    part1(input)
    part2(input)
