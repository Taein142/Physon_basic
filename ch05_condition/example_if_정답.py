# 정수를 입력받아 score변수와 같은지 확인하고, 같은면 “같습니다”를 출력하시오
score = 30
a = input("정수 입력> ")
a = int(a)
if a == score:
    print("같습니다")


# 하나의 수를 입력받아 음수이면 “음수 입력 금지”를 출력하시오
# a = input("수 입력> ")
# a = int(a)
# if a < 0:
#     print("음수 입력 금지")

# 2개의 정수를 입력받아 큰 수부터 출력하시오
# a = input("정수 입력> ")
# b = input("정수 입력> ")
# if a > b:
#     print(a,", ",b)
# else:
#     print(b,", ",a)

# 나이를 입력받아 19이상이면 “성인”, 미만이면 “청소년”을 출력하시오
# a = input("나이를 입력> ")
# a = int(a)
# if a >= 19:
#     print("성인")
# else:
#     print("청소년")

# 정수를 입력받아 score변수와 크기를 비교하시오
# score = 30
# a = input("정수 입력> ")
# a = int(a)
# if a > score:
#     print("크다")
# elif a == score:
#     print("같다")
# else:
#     print("작다")

# 점수를 입력받아 (100~90 ‘A’), (89~80 ‘B’), (79~70 ‘C’), (69~60 ‘D‘), (60미만 ’F’)를 출력하시오
# a = input("점수 입력> ")
# a = int(a)
# if a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# elif a < 60:
#     print("F")

# 2개의 주사위 정수를 입력받아 두수가 모두 4 이상이면 “이겼습니다”, 하나만 이상이면 “비겼습니다”, 둘 다 미만이면 “졌습니다”를 출력하시오
# a = input("첫 번째 주사위 수 입력> ")
# b = input("두 번째 주사위 수 입력> ")
# a = int(a)
# b = int(b)
# if a >= 4 and b >= 4:
#     print("이겼습니다")
# elif a >= 4 or b >= 4:
#     print("비겼습니다")
# else:
#     print("졌습니다")

# 정수 3개를 입력받아 그중 가장 큰 수를 출력하시오
# a = input("첫번째 수 입력> ")
# b = input("두번째 수 입력> ")
# c = input("세번째 수 입력> ")
# a = int(a)
# b = int(b)
# c = int(c)
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)

# 점수를 입력받아 (100~95 ‘A+’), (94~90 ‘A-’), (89~85 ‘B+’), (84~80 ‘B-‘), (79~75 ‘C+’), (74~70 ‘C-’), (69~65 ‘D+’), (64~60 ‘D-‘), (60미만 ’F’)를 출력하시오
# a = input("점수 입력> ")
# a = int(a)
# if a >= 90:
#     if a >= 95:
#         print("A+")
#     else:
#         print("A-")
# elif a >= 80:
#     if a >= 85:
#         print("B+")
#     else:
#         print("B-")
# elif a >= 70:
#     if a >= 75:
#         print("C+")
#     else:
#         print("C-")
# elif a >= 60:
#     if a >= 65:
#         print("D+")
#     else:
#         print("D-")
# else:
#     print("F")