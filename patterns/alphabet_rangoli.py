import string
def print_rangoli(size):
    # your code goes here
    l = []
    alpha = string.ascii_lowercase
    for i in range(1, size, 2): # start end increment
        print(str("-" * i).center(size, size))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# import string
# def rangoli_pattern(n):
#     L = []
#     alpha = string.ascii_lowercase
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))

# n = int(input("Enter the size of the pattern: "))
# rangoli_pattern(n)