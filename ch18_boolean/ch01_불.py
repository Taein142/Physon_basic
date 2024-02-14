# 불(bool) True / False
a = 10
b = 9

result1 = a == b
print("result1 :", result1)

result2 = a >= b
print("result2 :", result2)

result3 = a > b and result1
print("result3 :", result3)

result4 = result1 or result2
print("result4 :", result4)

result5 = not result4
print("result5 :", result5)

result6 = not (not a > b and result1)
print("result6 :", result6)

result7 = a in [1, 2, 3, 4, 5]
print("result7 :", result7)

result8 = a is b
print("result8 :", result8)

# 정수, 실수, 복소수, 문자열, 리스트[], 튜플(), 딕셔너리{'1':'일'}, 세트, 불