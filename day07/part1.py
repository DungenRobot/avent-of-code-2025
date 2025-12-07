

def print_grid(grid: list[str]):
    for line in grid:
        print(line)

def find_s(grid: list[str]) -> tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[0])):

            if grid[y][x] == 'S':
                return (x, y)
    return (-1, -1)



def main():

    grid: list[str] = []

    with open("day07/input.txt") as f:
        for line in f:
            grid.append(line.strip())
    

    splits = 0

    beam: set[tuple[int, int]] = set([find_s(grid)])

    for _ in range(len(grid) - 1):

        last_round = beam.copy()
        beam = set()

        for bx, by in last_round:

            by += 1

            char = grid[by][bx]

            if char == '^':

                splits += 1

                beam.add((bx + 1, by))
                beam.add((bx - 1, by))
            else:
                beam.add((bx, by))

                # I just realized we don't need to store the y position :P
                # TOO LATE!
    print(splits)

    


    




if __name__ == "__main__":
    main()