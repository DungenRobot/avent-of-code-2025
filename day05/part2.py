

def are_overlapping(r1: range, r2: range) -> bool:
    return r1.start in r2 or r1.stop in r2 or r2.start in r1



def main():
    with open("day05/input.txt") as f:

        fresh, _ = f.read().split('\n\n')

        ranges: list[range] = []

        for r in fresh.splitlines():

            start, end = r.split('-')

            ranges.append(range(int(start), int(end) + 1))


        #we first take out a range
        # then we compare it to all of the remaining ranges, merging along the way
        # if we have a merge, we remove that range from the list and go back through all remaining ranges
        # we do this until there are no merges
        #at this point the range is maximally merged and we can be satisfied that we're done with it

        max_merged: list[range] = []
        
        while len(ranges) > 0:
            x = ranges.pop()

            not_done = True

            while not_done:
                not_done = False
                for y in ranges.copy():
                    
                    if are_overlapping(x, y):
                        ranges.remove(y)
                        x = range(min(x.start, y.start), max(x.stop, y.stop))
                        not_done = True
            
            max_merged.append(x)

        
        print(sum([x.stop - x.start for x in max_merged]))



if __name__ == "__main__":
    main()