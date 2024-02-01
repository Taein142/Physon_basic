# print함수
a = 10
b = 20

print(a, " / ", b)
print(f"{a} / {b}")
print("{0} / {1}".format(a,b))
print("%d / %d" %(a, b))
print("-----------------------------------------")

# print 함수 end 옵션
print(a, " / ", b, end="|")
print(f"{a} / {b}", end="|")
print("{0} / {1}".format(a,b), end="|")
print("%d / %d" %(a, b))
print("-----------------------------------------")

# print 함수 sep 옵션
print(a, b, sep=" = ")
print("-----------------------------------------")