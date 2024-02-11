# 하나의 값을 입력받아 a변수에 있는지 판별하여 출력하시오.
# a = [1, 2, 3, 4]
# num = int(input("숫자 입력> "))
# if num in a:
#     print(num,"은/는 존재합니다")
# else:
#     print(num,"은/는 존재하지 않습니다")

# 반복적으로 과일을 입력받아 리스트에 추가하다가 0이 입력되면 입력을 중단하고, 짝수 번째에 입력된 값을 모두 출력하시오
# a = []
# cnt = 1
# while True:
#     fruit = input("과일 입력> ")
#     if fruit == '0':
#         break
#     elif cnt % 2 == 0:
#         a.append(fruit)
#     cnt += 1
# print(a)

# a = []
# while True:
#     fruit = input("과일 입력> ")
#     if fruit == '0':
#         break
#     else:
#         a.append(fruit)
# print(a[1::2])

# 반복적으로 정수를 입력받아 리스트에 추가하다가 0이 입력되면 입력을 중단하고, 0을 제외한 수를 입력한 반대순서로 출력하시오
# a = []
# while True:
#     num = input("정수 입력> ")
#     if num == "0":
#         break
#     a.append(num)
# a.reverse()
# for i in range(0, len(a)):
#     print(a[i])

# for i in range(len(a)-1,-1,-1):
#     print(a[i])


# 1~100사이 숫자 중 랜덤으로 9개를 뽑아 새로운 리스트를 만들고 출력하시오
# import random
# numbers = []
# for i in range(1, 10):
#     number = random.randint(1, 100)
#     numbers.append(number)
# print(numbers)

# 1~100사이 숫자 중 랜덤으로 10개를 뽑아 새로운 리스트를 만들고 최소값, 최대값을 출력하시오
# import random
# numbers = []
# for i in range(1, 11):
#     number = random.randint(1, 100)
#     numbers.append(number)
# print(numbers)
# maxNum = numbers[0]
# minNum = numbers[0]
# for i in range(0, 10):
#     if maxNum < numbers[i]:
#         maxNum = numbers[i]
#     if minNum > numbers[i]:
#         minNum = numbers[i]
# print("최대값: ", maxNum, " 최소값: ", minNum)

# 1~100사이 숫자 중 랜덤으로 짝수 10개를 뽑아 새로운 리스트를 만들고 출력하시오
# import random
# numbers = []
# a = 0
# while a < 10:
#     number = random.randint(1, 100)
#     if number % 2 == 0:
#         numbers.append(number)
#         a += 1
# print(numbers)

# 학생 이름을 무한으로 입력받다가 엔터를 치면 반복을멈추고 입력했던 값 모두를 출력하시오
# names = []
# while True:
#     name = input("이름입력> ")
#     if name != "":
#         names.append(name)
#     else:
#         break
# print(names)

# 5개의 성적을 입력받아 평균을 구하고 평균 이상인 학생 수를 출력하시오
# names = []
# for i in range(0, 5):
#     name = int(input("성적 입력> "))
#     names.append(name)
# avg = sum(names) / len(names)
# cnt = 0
# for i in range(0, 5):
#     if names[i] >= avg:
#         cnt += 1
# print(f"평균: {avg}, 평균 이상인 학생 수: {cnt}")

# 정수를 무한으로 입력받다가 0이 입력되면 입력을 종료하고, 입력받았던 정수를 오름차순으로 출력하시오
# 단) sort함수 사용x
# numList = []
# while True:
#     num = int(input("정수 입력> "))
#     if num == 0:
#         break
#     numList.append(num)

# for i in range(0, len(numList)-1):
#     for j in range(i+1, len(numList)):
#         if numList[i] > numList[j]:
#             temp = numList[i]
#             numList[i] = numList[j]
#             numList[j] = temp

# print(numList)