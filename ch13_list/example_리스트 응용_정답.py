# 아래 리스트를 활용하여 아래 출력예시와 같이 리스트를 만들고 출력하시오
# 출력예시) [['딸기', '포도', '복숭아'], ['사과', '바나나', '참외']]
a = ['딸기', '사과', '포도', '바나나', '복숭아', '참외']
a1 = []
a2 = []
a3 = []
for i in range(0, len(a), 2):
    a1.append(a[i])
    a2.append(a[i+1])
a3.append(a1)
a3.append(a2)
print(a3)

# 아래 리스트를 활용하여 아래 출력예시와 같이 리스트를 만들고 출력하시오 *enumerate()함수 사용
# 출력예시) [['딸기', '사과'], ['포도', '바나나'], ['복숭아', '참외']]
# b = ['딸기', '사과', '포도', '바나나', '복숭아', '참외']
# b1 = []
# b2 = []
# for i, j in enumerate(b):
#     b2.append(j)
#     if i % 2 != 0:
#         b1.append(b2)
#         b2 = []
# print(b1)