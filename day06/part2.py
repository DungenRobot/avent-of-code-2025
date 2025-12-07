import math
from collections import defaultdict

def get_operation_symbols(grid: list[str]) -> dict[int, str]:

    #Find the row that the operation symbols are in
    for y in range(len(grid)):
        if grid[y][0] in '+*':
            break
    
    out: dict[int, str] = {}
    
    #create a list of the x positions
    for x in range(len(grid[0])):
        if not grid[y][x] in '+*': continue # type: ignore
        out[x] = grid[y][x] # type: ignore

    return out



def get_numbers(grid: list[str], symbols: dict[int, str]) -> dict[int, list[int]]:

    visited_cells: set[tuple[int, int]] = set()
    numbers: dict[int, list[int]] = defaultdict(list)

    for y in range(len(grid)):
        for x in range(len(grid[0])):

            if (x, y) in visited_cells: continue

            visited_cells.add((x, y))

            char = grid[y][x]

            if char == ' ': continue

            if char in '+*': return numbers

            num = 0

            for j in range(y, len(grid)):
                visited_cells.add((x, j))

                if not grid[j][x] in '0123456789': break

                num = (num * 10) + int(grid[j][x])

            for i in range(x, -1, -1):
                if i in symbols.keys():
                    numbers[i].append(num)
                    break







    return numbers


def main():

    grid: list[str] = []

    with open("day06/input.txt") as f:
        for line in f:
            line = line.strip('\n')
            
            if line != '': grid.append(line)
    
    symbols = get_operation_symbols(grid)

    numbers = get_numbers(grid, symbols)

    total = 0

    for i, symbol in symbols.items():

        if symbol == '+':
            total += sum(numbers[i])
        else:
            total += math.prod(numbers[i])

    print(total)










if __name__ == "__main__":
    main()