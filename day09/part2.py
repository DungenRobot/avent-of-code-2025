




def main():

    tiles: list[tuple[int, int]] = []



    with open("day09/input.txt") as f:
        for line in f:
            x, y = line.strip().split(',')

            tiles.append((int(x), int(y)))
    
    all_tiles = tiles.copy()


    largest = 0

    while len(tiles) > 0:

        ax, ay = tiles.pop()

        for bx, by in tiles:

            #these values are tuned for my input
            #I would write code to automatically find them but I don't want to
            both_in_top = ay >= 50308 and by >= 50308
            both_in_bottom = ay <= 48457 and by <= 48457

            if not (both_in_bottom or both_in_top):
                continue


            area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)

            

            if area <= largest:
                continue


            # Thank you Fletcher
            # Go read this guy's writeup: https://fletcheaston.com/advent-of-code/2025/day-09

            all_green = True
            
            for tile_x, tile_y in all_tiles:
                if tile_x in range(min(ax, bx) + 1, max(ax, bx)) and tile_y in range(min(ay, by) + 1, max(ay, by)):

                    all_green = False

                    break

            if all_green:
                # Normally i'd take out print statements like these. But it's not one of those days
                print((ax, ay), (bx, by))
                largest = area
    print(largest)




if __name__ == "__main__":
    main()