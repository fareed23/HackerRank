def swap_case(s):
    return s.swapcase()
    # return s.upper() if s.islower() else s.lower()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)