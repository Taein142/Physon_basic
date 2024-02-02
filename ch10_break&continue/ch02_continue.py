#continue
for i in range(0, 10):
    if(i == 5):
        print()
        continue
    print(i)

#for i in range(0, 11):
#     if i % 2 == 0:
#         print("짝수 건너뛰기")
#         continue
#     print(i)

#while True:
#     num =  int(input("짝수 입력> "))
#     if(num == 0):
#         break
#     if(num % 2 == 0):
#         print(num)
#         continue
#     print("짝수를 입력해 주세요")

#import random
#while True:
#     a = random.randint(0, 100)
#     if a == 0:
#         print(a)
#         break
#     elif a % 2 == 0:
#         print()
#         continue
#     print(a)
#print("반복문 종료")