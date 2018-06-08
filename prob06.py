# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]
count = 0;
total = 0;
for num in data:
    if (num%3 == 0):
        count+=1
        total+=num
    else:
        pass
print("주어진 리스트에서 3의 배수의 개수=> ",count)
print("주어진 리스트에서 3의 배수의 합=> ",total)