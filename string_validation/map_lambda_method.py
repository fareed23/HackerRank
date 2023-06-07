if __name__ == '__main__':
    s = input()

# How the lambda function work?
# print True in list of map of lambda if n is n.isalnum() in s
print(True in list(map(lambda n:n.isalnum(), s)))
print(True in list(map(lambda n : n.isalpha(), s)))
print(True in list(map(lambda n : n.isdigit(), s)))
print(True in list(map(lambda n : n.islower(), s)))
print(True in list(map(lambda n : n.isupper(), s)))