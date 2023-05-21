lst = []
N = int(input()) 
for i in range(N):
    cmd = input().split() # insert 1 8 -> ['insert', '1', '8']
    if cmd[0] == 'insert':
        lst.insert(int(cmd[1]), int(cmd[2])) # As it is string we convert it into int
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'remove':
        lst.remove()
    elif cmd[0] == 'append':
        lst.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list.sort()
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'reverse':
        lst.reverse()
    else:
        print('invalid command')

