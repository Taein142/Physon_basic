# 항등(식별) 연산자 is, is not
a = 10
b = 10
print(a == b)
print(a is b)
print(a is not b)
print(id(a))
print(id(b))
print("---------")

aa = [1, 2, 3]
bb = [1, 2, 3]
print('(==)', aa == bb)
print('(is)', aa is bb)
print('(is not)', aa is not bb)
print(id(aa))
print(id(bb))