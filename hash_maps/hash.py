# Hash is used to compare the dictionary keys

# n = int(input())
# t = tuple(map(int,input().split()))
# # tu = tuple(t)
# print(hash(t))

n = int(input())
t = tuple(map(int, input().split()))
string_representation = ' '.join(map(str, t))
hash_value = hash(string_representation)
print(hash_value)

