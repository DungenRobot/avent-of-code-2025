


def find_largest_idx(line: str, start: int, end: int) -> int:

    largest = 0
    idx = start + 1

    for i in range(start + 1, end):
        if int(line[i]) > largest:
            idx = i
            largest = int(line[i])
    
    return idx

def main():
    with open("day03/input.txt") as f:

        total = 0

        for line in f:
            line = line.strip()

            subtotal = 0

            last_index = -1

            for iteration in range(12):

                idx = find_largest_idx(line, last_index, len(line) - (11 - iteration))

                subtotal *= 10

                subtotal += int(line[idx])

                last_index = idx

            print(subtotal)
            total += subtotal


        print(total)



if __name__ == "__main__":
    main()