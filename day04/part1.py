
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



def main():

    grid: list[str] = []

    with open("day04/input.txt") as f:

        for line in f:
            line = line.strip()

            grid.append(line)

    total = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] != '@':
                continue

            count = 0

            for di, dj in squares:

                y = i + di
                x = j + dj

                if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                    continue

                if grid[y][x] == '@':
                    count += 1
            
            if count < 4:
                total += 1
    print(total)





if __name__ == "__main__":
    main()