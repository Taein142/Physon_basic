# 리스트자료형의 매개변수를 받아 
# 모든 값을 더한 뒤 
# 리턴 하는 sumList함수 만들기

# 작성된 sumList함수를 사용(호출)하여 리턴 값을 출력하시오
# 출력 함수는 print()를 사용하시오
# ** 기존 파이썬 내장 함수인 sum함수는 사용하지 않습니다!

num1 = 10
num2 = 5

def sumList(a,b=None):
    if b is not None:
        return a*b
    return a*a

result = sumList(num1,num2)
print(result)

