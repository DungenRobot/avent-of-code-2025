



def main():

    total = 0
    dial= 50

    with open("day1/input.txt") as f:
        for line in f:

            dir = line[0]
            len = int(line[1:])

            if dir == 'R':
                dial += len
            else:
                dial -= len
            
            dial %= 100

            if dial == 0:
                total += 1
            

        print(total)






if __name__ == "__main__":
    main()