# 튜플(tuple)
f = ('딸기', '사과', '포도', '바나나','사과')
ff = '딸기', '사과', '포도', '바나나', '사과'
fff = '딸기',
print(type(f))
print(type(ff))
print(type(fff))

print(len(f)) # 길이
print(f[1]) # 인덱싱
print(f[1:]) # 슬라이싱
print(f*3) # 리스트 곱하기
print("-------------------------")

# f[1] = 4  # error
# del f[0]  # error
# f.append('수박')  # error
# f.insert(0, '멜론')  # error
# print(f.sort())  # error
# print(f.reverse())  # error
# f.remove('포도')  # error
# f.pop()  # error
# f = (4, 3, 2, 1) # 변경이아니라 새로운값을 대입하는것으로 가능
# print(f)

# print(f.index('사과'))
# print(f.count('사과'))

# if '포도' in f:
#     print("있다")
# else:
#     print("없다")

# for i in f:
#     print(i)

# for i in enumerate(f, 2): # 인덱스와 값을 튜플로 묶어주는 함수
#     print(i)

# for i, j in enumerate(f):
#     print(i," / ", j)

# 정수, 실수, 복소수, 문자열, 리스트[], 튜플(), 딕셔너리{'1':'일'}, 세트, 불