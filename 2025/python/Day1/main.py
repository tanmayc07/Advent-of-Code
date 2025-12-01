if __name__ == "__main__":
    with open("./input", "r") as f:
        data = f.read()

    lines = data.split("\n")

    direction = []
    value = []

    for line in lines:
        line = line.strip()
        if line != "":
            direction.append(line[:1])
            value.append(int(line[1:]))

    calc = [50]
    num_zero = 0  # Part 1
    num_crossings = 0  # Part 2
    itr = 0

    for dir, val in zip(direction, value):
        if dir == "L":
            curr = calc[itr]
            for v in range(1, val + 1):
                curr -= 1
                curr %= 100
                if curr == 0:
                    num_crossings += 1

            position = calc[itr] - val
            if position < 0:
                position = 100 - (abs(position) % 100)

            calc.append(position)
            itr += 1

        if dir == "R":
            curr = calc[itr]
            for v in range(1, val + 1):
                curr += 1
                curr %= 100
                if curr == 0:
                    num_crossings += 1

            position = calc[itr] + val
            if position >= 100:
                position = position % 100

            calc.append(position)
            itr += 1

    for c in calc:
        if c == 0 or c == 100:
            num_zero += 1

    # print(num_zero)
    print(num_crossings)
