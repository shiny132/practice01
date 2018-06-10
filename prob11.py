def sum(split):
    stack = 0
    for i in split:
        stack+=int(i)
    return stack
s = input()
split = ''.join(s).split(" ")
re = sum(split)
print(re)