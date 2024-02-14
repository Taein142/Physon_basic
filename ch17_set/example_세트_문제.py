# 아래 변수의 값들 중 곂치는 값을 두배로 변경하시오
# 출력예시) a => {1, 2, 6, 8, 10}
#          b => {6, 7, 8, 10}
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
for i in a & b:
    a.remove(i)
    a.add(i*2)
    b.remove(i)
    b.add(i)
print(a)
print(b)


# random함수를 활용하여 1~45의 겹치지 않는 랜덤수를 6개 뽑아 세트자료형을 만드시오
import random     # *랜덤숫자 뽑는 문법 : num = random.randint(1,45)
a = set()
while True:
    num = random.randint(1,45)
    print(num)
    a.add(num)
    if len(a) == 6:
        break

while len(a) < 6:
    num = random.randint(1,45)
    a.add(num)
print(a)