# 반복적으로 과일을 입력받아 리스트에 추가하다가 0이 입력되면 입력을 중단하고, 짝수 번째에 입력된 값을 모두 출력하시오
# 입력예시)
#   과일 입력> 사과
#   과일 입력> 배
#   과일 입력> 수박
#   과일 입력> 멜론
#   과일 입력> 바나나
#   과일 입력> 0
# 출력예시) 
#   ['배', '멜론']

a = []
while True:
    fruit = input("과일 입력> ")
    if fruit == '0':
        break
    else:
        a.append(fruit)
print(a[1::2])

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

# a변수를 활용하여 아래 출력예시와 같이 출력하시오 *반복문사용
# 출력예시) 딸기,사과,포도,바나나
# a = ['딸기', '사과', '포도', '바나나']
# for i in a:
#     if i == a[len(a) - 1]:
#         print(i)
#         break
#     print(i, end=",")

# 찾을 값과 변경할 값을 입력받아 찾은 모든값을 변경하고 출력하시오
# a = ['딸기', '사과', '포도', '바나나', '바나나', '멜론', '키위', '바나나']
# find = input("찾을 값 입력> ")
# change = input("변경할 값 입력> ")
# for i in range(0, len(a)):
#     if a[i] == find:
#         a[i] = change
# print(a)