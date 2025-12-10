





def main():

    tiles: list[tuple[int, int]] = []

    with open("day09/input.txt") as f:
        for line in f:
            x, y = line.strip().split(',')

            tiles.append((int(x), int(y)))
    
    largest = 0

    while len(tiles) > 0:

        ax, ay = tiles.pop()

        for bx, by in tiles:

            area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)

            if area > largest:
                largest = area
    
    print(largest)



if __name__ == "__main__":
    main()