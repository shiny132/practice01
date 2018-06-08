# 주어진 if 문을 dict를 사용해서 수정하세요.
menu = input()

keys = ("오뎅", "순대", "만두", "없음")
values = (300, 400, 500, 0)
dic = dict(zip(keys, values))
if(menu!= "오뎅"or"순대"or"만두"):
    menu = "없음"

print("가격 : {0}".format(dic.get(menu)))