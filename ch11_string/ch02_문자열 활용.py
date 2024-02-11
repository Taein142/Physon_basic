# 문자열 활용
a = "파이썬은 너무나 즐거워"

start = input("시작문자 입력> ")
end = input("종료문자 입력> ")
print(a[a.index(start) : a.index(end)+1])

# cnt = 0
# for i in a:
#     if i == " ":
#         cnt += 1
# print(f"공백은 {cnt}개")

# for i in range(0, len(a)):
#     if a[i] == " ":
#         print(f"공백 인덱스는 : {i}")