# 1) 다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
result = s.replace(',', '').replace('.', '').replace('\n', '').upper()
c_result = result.split(" ")
result = list(set(c_result))
result.sort()
for a in result:
    print(a)
print("-----------------------------------")
# 2)각 단어의 빈도수도 함께 출력해 보세요
count = {}
for split in c_result:
    if split in count.keys():
        count[split] += 1
    else:
        count[split] = 1
for key, value in count.items():
    print(str(key) + ":" + str(value))
    # or print(key,":",value)