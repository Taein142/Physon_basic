# input함수
a = input("숫자만 입력> ")
print(a)
print(type(a))
print(type(int(a)))

print(f"변경 전 : {type(a)}, 변경 후 : {type(int(a))}")