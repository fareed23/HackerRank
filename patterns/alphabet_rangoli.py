import string
def rangoli_pattern(n):
    # your code goes here
    L = []
    alpha = string.ascii_lowercase
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

n = int(input("Enter the size of the pattern: "))
rangoli_pattern(n)