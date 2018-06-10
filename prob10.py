menu = input()
print(menu, type(menu))
print(menu == "오뎅")
keys = ("오뎅", "순대", "만두", "없음")
values = (300, 400, 500, 0)
dic = dict(zip(keys, values))
if(menu!= "오뎅" and menu!="순대" and menu!="만두"):
    print('a')
    menu = "없음"

print("가격 : {}".format(dic[menu]))