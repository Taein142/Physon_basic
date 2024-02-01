# 잇츠캠퍼스에서 실행시 input 이 있는 경우
# 하단 입력창에 값을 넣어주세요.
# 예) input 이 3개 인 경우, 엔터로 구분하여 3개 입력
# 값 1
# 값 2
# 값 3

# 하나의 정수를 입력받아 1부터 입력받은 수까지 출력하시오 *range함수사용
a = input("정수 입력> ")
a = int(a)
for i in range(1,a+1):
    print(i)

# 하나의 정수를 입력받아 1부터 입력받은 수까지의 합을 출력하시오 *range함수사용
# a = int(input("정수 입력> "))
# sum = 0
# for i in range(1, a+1):
#     sum = sum+i
# print(sum)

# 하나의 정수를 입력받아 1부터 입력받은 수까지 짝수의 개수를 출력하시오 *range함수사용
# a = int(input("정수 입력> "))
# cnt = 0
# for i in range(1, a+1):
#     if i % 2 == 0:
#         cnt += 1
# print(cnt)

# 5개의 수를 입력받아 가장 큰 수를 출력하시오
# maxNum = 0
# for i in range(0, 5):
#     num = int(input("수 입력> "))
#     if num > maxNum:
#         maxNum = num
# print(maxNum)