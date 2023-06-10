def split_and_join(line):
    # write your code here
    spl = line.split(" ")
    a = "-".join(spl)
    return a
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
