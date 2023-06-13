def print_rangoli(size):
    # your code goes here
    for i in range(1, size, 2):
        print(str("-" * i).center(size, size))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)