if __name__ == '__main__':
    s = input()

# Using if-else method
res = False
for i in s:
    if i.isalnum():
        res = True
        break
print(res)

for j in s:
    if j.isalpha():
        res = True
        break
print(res)


for k in s:
    if k.isdigit():
        res = True
        break
print(res)

for l in s:
    if l.islower():
        res = True
        break
print(res)


for m in s:
    if m.isupper():
        res = True
        break
print(res)
