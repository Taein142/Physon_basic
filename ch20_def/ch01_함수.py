# 함수
def justPrint():
    print('안녕하세요')
justPrint()
result1 = justPrint()
print('result1 :',result1)
print('-'*30)

# def printParam(a):
#     print(a)
# printParam("파이썬은 즐거워")
# result2 = printParam("파이썬이란?")
# print('result2 :',result2)
# # printParam() # 매개변수에 값이 전달되지 않으면 error
# print('-'*30)

# def pythonReturn():
#     return '파이썬'
# result3 = pythonReturn()
# print('result3 :',result3)
# print(pythonReturn())
# # print(pythonReturn('값전달')) # 매개변수가 없는데 값이 전달되면 error
# print('-'*30)

# def plus(a, b):
#     return a+b
# result4 = plus(1, 3)
# print('result4 :',result4)
# print(plus(5,7))
# print('-'*30)

# def manyParam(*args): # 몇개의 매개변수를 받을 지 모를때는 변수 앞에 '*'를 붙여준다.
#     print(type(args)) # *튜플로 저장
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(manyParam(1,2,3,4,5,6,7,8,9,10))
# print(manyParam(1,2,3,4,5))
# print('-'*30)

# def dictParam(**kwargs):
#     print(kwargs)
# dictParam(a = 'A')
# dictParam(a = 'A', b = 'B')
# print('-'*30)

# def default_value1(a = "안녕"):
#     print("default_value1함수 호출됨", a)
# default_value1('파이썬')
# default_value1()
# print('-'*30)

# def default_value2(a, b = "안녕"): # 매개변수가 여러가지일 경우엔 default값은 뒤쪽에 위치해야함
#     print("default_value2함수 호출됨", a, b)
# default_value2("가자")
# default_value2("바다로", "떠나자")