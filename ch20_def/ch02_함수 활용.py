# 함수 활용
def plus(a, b):
    return a + b
print(plus(10, 4))
print('-'*30)

# def minus(a, b):
#     return a - b
# print(minus(10, 4))
# print('-'*30)

# def multiplication(a, b = None):
#     if b is None:
#         return a * a
#     return a * b
# print(multiplication(5))
# print(multiplication(3, 4))
# print('-'*30)

# def division(a, b):
#     if b == 0:
#         return "0으로는 나눌 수 없습니다"
#     return a / b
# print(division(4, 3))
# print('-'*30)

# import datetime
# def dayCheck(y, m, d):
#     day = datetime.date(y, m, d)
#     print(day)
#     return day.strftime("%A") 
# print(dayCheck(2022, 12, 15))