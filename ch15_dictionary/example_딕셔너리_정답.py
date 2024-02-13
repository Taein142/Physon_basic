# 키가 1~10, 값이 10~1까지의 딕셔너리를 만드시오
b = {}
for i in range(1, 11):
    b[i] = 11-i
print(b)

# 딕셔너리를 하나 선언하고, 키와 값이 같은 딕셔너리 쌍이 몇개인지 출력하시오
# c = {"a":"A", "b":"b", "C":"C", "d":"D", "E":"E"}
# cnt = 0
# for i, j in c.items():
#     if i == j:
#         cnt += 1
# print(f"키와 값이 같은 쌍은 {cnt}개 입니다")