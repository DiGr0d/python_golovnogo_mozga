n, m, q, cw, sw, hw, tw = map(int, input().split())
flag = True
average = 0
first = -1
firstname = ''
second = -1
secondname = ''
third = -1
thirdname = ''
last = float('inf')
for j in range(n):
    name = input()
    sum = 0
    if m > 0 and cw > 0 and sw > 0 and hw > 0 and tw > 0 and n >= 3:
        for i in range(m):
            ai, bi, ci, di = map(int, input().split(','))
            sum += ai * cw + bi * sw + ci * hw + tw * di
        if sum > q:
            flag = False
            break
    else:
        flag = False
        break
    rate = sum / q * 100
    average += rate
    if sum > third and sum <= second:
        third = sum
        thirdname = name
    elif sum > second and sum <= first:
        third = second
        thirdname = secondname
        second = sum
        secondname = name
    elif sum > first:
        third = second
        thirdname = secondname
        second = first
        secondname = firstname
        first = sum
        firstname = name
    if sum <= last:
        last = sum
average /= n
if flag is True:
    first, second, third, last = map(lambda x: round(x / q * 100), [first, second, third, last])
    print(round(first), round(average), round(last))
    print(f"{firstname} {first}%")
    print(f"{secondname} {second}%")
    print(f"{thirdname} {third}%")
    if average <= 50:
        print("Курс усваивается плохо")
    else:
        print("Курс усваивается хорошо")
else:
    print("Во введённых данных ошибка")
