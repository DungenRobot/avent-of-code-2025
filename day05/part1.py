
def main():
    with open("day05/input.txt") as f:

        fresh, ids = f.read().split('\n\n')

        ranges: list[range] = []

        for r in fresh.splitlines():

            s, e = r.split('-')

            ranges.append(range(int(s), int(e) + 1))
        

        total = 0

        for id in ids.splitlines():
            for r in ranges:
                if int(id) in r:
                    total += 1
                    break

        
        print(total)



if __name__ == "__main__":
    main()