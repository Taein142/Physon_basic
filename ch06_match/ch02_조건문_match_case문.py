# 조건문 match_case
num = int(input("1~3숫자입력> "))
match num:
    case 1:
        print("1 입력")
    case 2:
        print("2 입력")
    case 3:
        print("3 입력")
    case _:
        print('1~3이외의 숫자')

# num1 = int(input("10 입력> "))
# num2 = int(input("7 입력> "))
# match num1, num2:
#     case 10, 7:
#         print("num1 = 10, num2 = 7")
#     case 10, _:
#         print("num1 = 10")
#     case _, 7:
#         print("num2 = 7")
#     case _:
#         print("num1 = ?, num2 = ?")

# num1 = int(input("짝수 입력> "))
# num2 = int(input("홀수 입력> "))
# match num1 % 2, num2 % 2:
#     case 0, 1:
#         print("num1짝수 num2홀수")
#     case 0, _:
#         print("num1짝수")
#     case _, 1:
#         print("num2홀수")
#     case _:
#         print("둘 다 다름")