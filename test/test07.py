import datetime
import math
import random

# 난이도 하) 현재 날짜와 시간을 출력하시오
current_time = datetime.datetime.now()
print(current_time)

# 난이도 중) 임의의 실수를 올림 하여 출력하시오 **예) 5.2(실수)을 6으로 출력
floatNumber = random.uniform(1.0,10.0)
rounded_number = math.ceil(floatNumber)
print(rounded_number)

# print("ㅡ"*30)

# 난이도 상) for문을 사용하여 1~100까지의 랜덤 숫자를 5개 출력하시오
for i in range(5):
    number = random.randint(1,100)
    print(number)