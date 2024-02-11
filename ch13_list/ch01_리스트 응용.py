# 리스트 응용
a = [['딸기', '사과'], ['포도', '바나나'],['수박', '귤', '참외']]
print(a[2][2])
print(a[1:])

# b = [['딸기', '사과'], ['포도', '바나나',['수박', '귤', '참외']]]
# print(b[1][2][1])
# print(b[::2])
# print(b[1][::2])

# c = ['딸기', '사과', '포도', '바나나']
# for i in enumerate(c): # 인덱스와 값을 튜플로 묶어주는 함수
#     print(i)

# c = ['딸기', '사과', '포도', '바나나']
# for i, j in enumerate(c):
#     print(i," / ", j)

# 컴프리헨션으로 리스트 만들기
# d = [x for x in range(0, 10)]
# print(d)
# d1 = [x for x in range(0, 10) if x!=3]
# print(d1)  
# d2 = [[x,y] for x in range(2, 10) for y in range(1, 10)]
# print(d2)  

# 출력예시) [[0, '딸기'], [1, '사과'], [2, '포도'], [3, '바나나']]
# e = ['딸기', '사과', '포도', '바나나']
# e1 = []
# for i in enumerate(e):
#     e1.append(list(i))
# print(e1)

# e2 = [[i, j] for i, j in enumerate(e)]
# print(e2)

# # 출력예시) ['사과', '딸기', '바나나', '포도']
# e = ['딸기', '사과', '포도', '바나나']
# for i, j in enumerate(e):
#     if i % 2 == 0:
#         e.insert(i+2, e[i])
#         del e[i]
# print(e)

# for i in range(0, len(e), 2):
#     e.insert(i+1, e.pop(i))
# print(e)