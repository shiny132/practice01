# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# ‘usr’, ‘local’, ‘bin’, ‘python’
# ‘/usr/local/‘bin’, ‘python’
s = '/usr/local/bin/python'
result = s.split("/")
result = result[1:]
print('\'{}\',\'{}\',\'{}\',\'{}\''.format(result[0],result[1],result[2],result[3]))
# 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.
print('\'/{}/{}/\'{}\', \'{}\''.format(result[0],result[1],result[2],result[3]))