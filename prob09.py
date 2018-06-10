def reverse(s):
    stack = []
    for i in s[::-1]:
        stack.append(i)
    return stack
s = list(input())
stack = ''.join(reverse(s))
print(stack)