
squares = [
    (1, 1),
    (1, 0),
    (0, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 1)
]

def can_be_removed(grid: list[str], i: int, j: int) -> bool:

    count = 0

    for di, dj in squares:
        y = i + di
        x = j + dj

        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            continue

        if grid[y][x] == '@':
            count += 1

    return count < 4



def main():

    grid: list[str] = []

    with open("day04/input.txt") as f:

        for line in f:
            line = line.strip()

            grid.append(line)

    total = 0
    rolls_were_removed = True


    while rolls_were_removed:

        rolls_were_removed = False

        to_remove: list[tuple[int, int]] = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] != '@':
                    continue

                if can_be_removed(grid, i, j):
                    total += 1
                    to_remove.append((i, j))
                    rolls_were_removed = True
        
        for i, j in to_remove:
            # I truly hate this. Why is python like this
            grid[i] = grid[i][:j] + 'x' + grid[i][j + 1:]



    print(total)





if __name__ == "__main__":
    main()