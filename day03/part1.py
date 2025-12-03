

def main():
    with open("day03/input.txt") as f:

        total = 0

        for line in f:
            line = line.strip()

            tens = 0
            ten_index = -1

            for i in range(len(line) - 1):

                x = int(line[i])

                if x > tens:
                    tens = x
                    ten_index = i

                if tens == 9:
                    break
            
            ones = 0   

            for i in range(ten_index + 1, len(line)):

                x = int(line[i])

                ones = max(x, ones)

                if ones == 9:
                    break
            
            num = tens * 10 + ones
            print(num)
            total += num
        print(total)



if __name__ == "__main__":
    main()