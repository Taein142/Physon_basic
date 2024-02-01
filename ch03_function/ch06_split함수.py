# split함수
a = "a, b, c, d, e"
# b = "a,b,c,d,e"

print(a)
print(a.split())
print(a.split(","))
print(a.split(",",3)) # (sep=',', maxsplit=3)
# print(a.split(sep=",", maxsplit=3))

print(f"공백 : {a.split()}, 콤마 : {a.split(',')}, 콤마3개만 : {a.split(',',3)}")