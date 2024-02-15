# 참조주소
a = '홍길동'
print(a)
print(f"a 변경전 => {id(a)}")
a = '김길동'
print(a)
print(f"a 변경후 => {id(a)}")
print('-'*30)

# b1 = '파이썬'
# b2 = '파이썬'
# print(b1, b2)
# print(f"id(b1) => {id(b1)}")
# print(f"id(b2) => {id(b2)}")
# print('-'*30)

# c1 = 55
# c2 = c1
# print(c1, c2)
# print(f"id(c1) => {id(c1)}")
# print(f"id(c2) => {id(c2)}")
# print('-'*30)

# d = ['a', 'b', 'c']
# print(d)
# print(f"d 변경전 => {id(d)}")
# d[2] = 'z'
# print(d)
# print(f"d 변경후 => {id(d)}")
# print('-'*30)

# e = ['a', 'b', 'c']
# e1 = e[0]
# print(e1, e[0])
# print(f"id(e1) => {id(e1)}")
# print(f"id(e[0]) => {id(e[0])}")
# print('-'*30)

# f1 = ['a', 'b', 'c']
# f2 = f1
# print(f1, f2)
# print(f"id(f1) => {id(f1)}")
# print(f"id(f2) => {id(f2)}")

# f1[2] = 'z'
# print(f1, f2)