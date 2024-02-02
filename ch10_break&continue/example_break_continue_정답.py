# 1~100사이 숫자를 반복하면서 뽑고 100이 뽑이면 반복을 종료하고, 반복문이 몇번 돌았는지 출력하시오
import random
cnt = 0
while True:
    a = random.randint(1, 100)
    cnt = cnt+1
    if a == 100:
        break
print(cnt, "번 반복했습니다")

# 무한의 정수를 입력받다가 0이 입력되면 입력을 중단하고, 짝수 번째에 입력된 값의 합을 출력하시오
#numSum = 0
#cnt = 1
#while True:
#     num = int(input("정수 입력> "))
#     if num == 0:
#         break
#     elif cnt % 2 == 0:
#         numSum += num
#     cnt += 1
#print(numSum)

# 1~31까지의 숫자 하나를 랜덤으로 뽑고, 반복하면서 입력받다가 
# 입력값이 뽑은 랜덤 수보다 작으면 ‘정답은 더 큰 값 입니다’, 
# 크면 ‘정답은 더 작은 값 입니다’, 
# 같으면 '정답'출력 후 반복문 종료
#import random
#answer = random.randint(1, 31)
#while True:
#     num = int(input("숫자 입력> "))
#     if num == answer:
#         print("정답입니다!! 정답:", answer)
#         break
#     elif num > answer:
#         print("정답은 더 작은 값 입니다")
#     elif num < answer:
#         print("정답은 더 큰 값 입니다")