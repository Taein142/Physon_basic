# 딕셔너리 응용
a = {"일":1, "이":2, "삼":3, "사":4, "오":5}

# 딕셔너리 에러 예 - 딕셔너리는 반복중에 변경이 허용되지 않는다.
for i in a.keys():
    if a[i] == 3:
        del a[i]
        break
    print(i)
print(a)

# for i in list(a.keys()):
#     if a[i] <= 3:
#         del a[i]
# print(a)

# b = ['a', 'b', 'c', 'd']
# b1 = {}
# for i, j in enumerate(b):  
#     b1[i] = j # d.setdefault(i, j)
# print("b1", b1)

# b2 = {i : j for i, j in enumerate(b)} # 컴프리헨션
# print("b2", b2)

# b = ['a', 'b', 'c', 'd']
# c = ['A', 'B', 'C', 'D']
# for i in zip(b, c): # 각 인자를 순서대로 튜플로 묶어주는 함수
#     print(i)

# for i, j in zip(b, c): 
#     print(i, j)

# print(dict(zip(b, c))) # zip함수로 딕셔너리 만들기