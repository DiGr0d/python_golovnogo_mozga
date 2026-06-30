#польский калькулятор
str = input()
cur = 0
stack = []
flag = False
for ch in str:
    if ch.isdigit():
        cur = cur * 10 + int(ch)
        flag = True
        continue
    if flag is True:
        stack.append(cur)
        flag = False
    cur = 0
    if ch == ' ':
        continue
    if ch in "*+-/":
        first = stack.pop()
        second = stack.pop()
    if ch in "~!#":
        first = stack.pop()
    if ch in "@":
        first = stack.pop()
        second = stack.pop()
        third = stack.pop()
    match ch:
        case '*':
            stack.append(first * second)
        case '+':
            stack.append(first + second)
        case '-':
            stack.append(second - first)
        case '/':
            stack.append(second // first)
        case '~':
            stack.append(-first)
        case '!':
            k = 1
            for j in range(1, first + 1):
                k *= j
            stack.append(k)
        case '#':
            stack.append(first)
            stack.append(first)
        case '@':
            for _ in map(lambda t: stack.append(t), [second, first, third]):
                pass
print(stack[-1])