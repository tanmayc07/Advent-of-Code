from typing import Tuple


def read_input(file: str) -> Tuple[list[str], list[str]]:
    with open(file, "r") as f:
        contents = f.read()

    contents = contents.strip().split("\n")
    ranges: list[str] = []
    ids: list[str] = []
    br_idx = 0
    for idx, lines in enumerate(contents):
        if lines == "":
            br_idx = idx + 1
            break
        ranges.append(lines)

    for idx in range(br_idx, len(contents)):
        ids.append(contents[idx])

    return (ranges, ids)


def part1(input: Tuple[list[str], list[str]]):
    ranges, ids = input

    range_list: list[range] = []
    for r in ranges:
        a, b = int(r.split("-")[0]), int(r.split("-")[1])
        first = min(a, b)
        second = max(a, b)
        range_list.append(range(first, second + 1))

    num_fresh = 0
    for id in ids:
        for r in range_list:
            if int(id) in r:
                num_fresh += 1
                break

    print(num_fresh)


def part2(input: Tuple[list[str], list[str]]):
    ranges, _ = input

    range_list: list[range] = []
    for r in ranges:
        a, b = int(r.split("-")[0]), int(r.split("-")[1])
        first = min(a, b)
        second = max(a, b)
        range_list.append(range(first, second + 1))

    range_list = sorted(range_list, key=lambda x: x.start)
    new_range_list = []
    i = 0
    N = len(range_list)

    while i < N:
        current_range = range_list[i]

        current_start = current_range.start
        current_stop = current_range.stop

        while (i + 1) < N and (range_list[i + 1].start <= current_stop):
            next = range_list[i + 1]
            current_stop = max(current_stop, next.stop)
            i += 1

        new_range_list.append(range(current_start, current_stop))
        i += 1

    num_ing_ids = 0
    for rng in new_range_list:
        num_ing_ids += rng.stop - rng.start

    print(num_ing_ids)


if __name__ == "__main__":
    file = "input"
    input = read_input(file)

    part1(input)
    part2(input)
