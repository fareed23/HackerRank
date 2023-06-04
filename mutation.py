# Method 1 through converting into a list and then change

def mutate_string(string, position, character):
    lst = list(string) # convert string into a list 
    lst[position] = character # assign character at the specified position
    name = ''.join(lst) # join the list back into a string
    return name


# Method 2 through slicing

def mutate_string(string, position, character):
    lst = list(string)
    name = string[:position] + character + string[position:]
    return name



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)