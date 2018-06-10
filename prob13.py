s = int(input("숫자를 입력하세요: "))
total = 0
if s % 2 == 0:
    for i in range(s+1):
        if i % 2 == 0:
            total += i
else:
    for i in range(s+1):
        if i % 2 != 0:
            total += i
print("결과 값: {}".format(total))