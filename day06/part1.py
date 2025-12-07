from collections import defaultdict
import math

def main():

    columns: dict[int, list[int]] = defaultdict(list)
    total = 0

    with open("day06/input.txt") as f:
        for line in f:
            line = line.split()

            for i, x in enumerate(line):

                if x == '*':

                    total += math.prod(columns[i])

                    continue
                
                if x == '+':
                    
                    total += sum(columns[i])
                    continue

                x = int(x)

                columns[i].append(x)
    print(total)




if __name__ == "__main__":
    main()