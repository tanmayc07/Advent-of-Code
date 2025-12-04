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
    st = []
    sum_joltage = 0

    for line in input:
        deletions = len(line) - 12
        nums = list(line)

        st.append(nums[0])
        for idx in range(1, len(nums)):
            while deletions > 0 and len(st) > 0 and st[-1] < nums[idx]:
                st.pop()
                deletions -= 1
            st.append(nums[idx])

        while deletions > 0:
            st.pop()
            deletions -= 1

        sum_joltage += int("".join(st))
        st = []

    print(sum_joltage)


if __name__ == "__main__":
    file = str("input")
    data = read_input(file)

    part1(data)
    part2(data)
