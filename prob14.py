import random
count = 0
while(True):
    if count == 0:
        print("수를 결정하였습니다. 맞추어보세요\n 1-100")
        ran = random.randrange(1,101)
    count+=1
    s = int(input("{}>>".format(count)))
    if s > ran:
        print("더 낮게")
    elif s < ran:
        print("더 높게")
    else:
        yn = input("맞았습니다.\n 다시 하시겠습니까(y/n)>>")
        if yn == 'y':
            count=0
        else:
            break
        