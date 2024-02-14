# 아래 리스트에서 True인 값들만 모아 새로운 리스트를 만드시오
# 출력예시) [{'a': 'A'}, 5, '안녕']
a = [[], 0, {'a':'A'}, 5, "안녕", ""]
a1 = []

for i in a:
    if True == bool(i):
        a1.append(i)
print(a1)

