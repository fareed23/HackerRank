if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # lst = list(arr)
    # Convert into a list first 
    scores = list(arr)

    # Sort the list in ascending order
    # No variable needed for the sort() function
    scores.sort()

    first, second = -100, -100 # set to the min values from constraints

    for score in scores:
        if first < score:
            second = first # Pass value to second
            first = score # Then update first

    print(second)
    #     else:
    #         continue
    # order = sorted(scores, reverse=True)
    # print(order[1])

    
    
# print(sorted(set(arr), reverse=True)[1])
