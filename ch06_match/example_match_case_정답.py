# 하나의 수를 입력받고, 그 수가 3,5의 배수인지 확인하여 '3과5의배수', '3의배수' '5의배수' '둘다아님'을 출력하시오
num = int(input("숫자입력> "))
match num%3, num%5:
    case 0, 0:
        print("3과5의 배수")
    case 0, _:
        print("3의배수")
    case _, 0:
        print("5의배수")
    case _:
        print('둘다아님')