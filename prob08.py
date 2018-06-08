# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
lst = []
result = 0
for i in range(5):
    a = int(input())
    lst.append(a)
for index in lst:
    result += index
print("평균 :",result/len(lst))

