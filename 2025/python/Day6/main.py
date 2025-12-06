import copy


def read_input(file: str) -> list[str]:
    with open(file, "r") as f:
        contents = f.read()

    contents = contents.strip().split("\n")

    return contents


def read_input2(file: str) -> list[str]:
    with open(file, "r") as f:
        contents = f.read()

    contents = contents.split("\n")

    return contents


def part1(input: list[str]):
    filtered_inp = []  # To save the numbers like [['123', '328', '51', '64'], ['45', '64', '387', '23']...]
    for line in input:
        line = line.split(" ")
        filtered_inp.append([word for word in line if word != ""])

    ops = filtered_inp[-1]  # operators list
    result = 0
    for idx, op in enumerate(ops):
        match op:
            case "+":
                sum = 0
                row: int = 0
                while row < len(filtered_inp) - 1:
                    num = int(filtered_inp[row][idx])
                    sum += num
                    row += 1
                result += sum
            case "*":
                mul = 1
                row: int = 0
                while row < len(filtered_inp) - 1:
                    num = int(filtered_inp[row][idx])
                    mul *= num
                    row += 1
                result += mul

    print(result)


def part2(input: list[str]):
    processed = []
    for line in input:
        line += " "
        processed.append(list(line))

    processed = processed[:-1]

    ops = processed[-1]  # Operators list
    num_d = copy.deepcopy(
        ops
    )  # List to store max number of digits for the column of operator
    for i in range(len(ops)):
        st = i
        while st + 1 < len(ops) and ops[st + 1] == " ":
            st += 1
        num_d[i] = st - i
        i = st + 1

    result = 0
    for idx, op in enumerate(ops):
        match op:
            case "+":
                col = idx
                nd = num_d[idx]
                sum = 0
                while nd > 0:
                    row = 0
                    curr = []
                    # Join the digits vertically to produce the number
                    while row < len(processed) - 1:
                        if col < len(processed[row]) and processed[row][col] != " ":
                            curr.append(processed[row][col])
                        row += 1
                    num = int("".join(curr))
                    sum += num  # Perform the operation
                    nd -= 1
                    col += 1
                result += sum

            case "*":
                nd = num_d[idx]
                mul = 1
                col = idx
                while nd > 0:
                    row = 0
                    curr = []
                    while row < len(processed) - 1:
                        if col < len(processed[row]) and processed[row][col] != " ":
                            curr.append(processed[row][col])
                        row += 1
                    num = int("".join(curr))
                    mul *= num
                    nd -= 1
                    col += 1
                result += mul
    print(result)


if __name__ == "__main__":
    file = "test"
    input = read_input(file)
    input2 = read_input2(file)

    part1(input)
    part2(input2)
