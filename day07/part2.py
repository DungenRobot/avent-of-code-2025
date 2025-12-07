from part1 import find_s
from collections import defaultdict


def main():

    grid: list[str] = []

    with open("day07/input.txt") as f:
        for line in f:
            grid.append(line.strip())
    

    start_x, _ = find_s(grid)

    beam: dict[int, int] = defaultdict(int)

    beam[start_x] = 1

    for y in range(len(grid) - 1):

        last_round = beam.copy()
        beam = defaultdict(int)
        
        # T is the number of timelines this beam exists in

        for bx, T in last_round.items():

            by = y + 1

            char = grid[by][bx]

            # Basically every time we overlap with another beam we add the two timeline values together

            if char == '^':

                beam[bx + 1] += T
                beam[bx - 1] += T
            else:
                beam[bx] += T

    print(sum(beam.values()))


    




if __name__ == "__main__":
    main()