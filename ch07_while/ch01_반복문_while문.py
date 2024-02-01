# 반복문 while
a = 1
while a < 10:
    print(a)
    a += 1
print("반복문 종료")

num = int(input("숫자입력> "))
while num != 0:
    print(num)
    num = int(input("숫자입력> "))
    print("반복문 종료")

run = True
while run:
    num = int(input("숫자 입력> "))
    print(num)
    if num == 0:
        run = False
print("반복문 종료")

a = ["안녕", "헬로", "니하오", "콘니치와"]
aa = input("인사말 입력> ")
while aa in a:
    print(aa)
    aa = input("인사말 입력> ")
print("없는 인사말 입니다")