if __name__ == '__main__':
    s = input()

# Using for loop method
strr = list(s)

al_num = False
alp = False
dig = False
low = False
up = False

for i in strr:
    al_num = al_num or i.isalnum()
    alp = alp or i.isalpha()
    dig = dig or i.isdigit()
    low = low or i.islower()
    up = up or i.isupper()


print(al_num)
print(alp)
print(dig)
print(low)
print(up)