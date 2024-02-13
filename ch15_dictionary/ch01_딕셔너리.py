# 딕셔너리(dict)
g = {"대한민국":"서울", "미국":"워싱턴", "중국":"베이징"}

print(g["대한민국"]) # 값 얻기
g["일본"] = "도쿄" # 추가 - 키가 없으면 추가
print(g)
g["미국"] = "워싱턴 D.C" # 수정 - 키가 있으면 수정
print(g)
del g["중국"] # 삭제
print(g)
print("-----------------")

# print(g.get("대한민국", "없음")) # 값 얻기 * 키가 없으면 None 또는 두번째 인자 리턴
# g.setdefault("캐나다","오타와") # 추가 - 변경은 안됨
# print(g)
# g.update(캐나다 = "오타니") # 키가 있으면 수정, 없으면 추가
# print(g)
# g.update(캐나다 = "오타", 프랑스 = "파리")
# print(g)
# g.update({"캐나다":"오타와", "독일":"베를린"}) # 딕셔너리로 수정
# print(g) 
# g.update([["미국","워싱턴"],["태국","방콕"]]) # 리스트로 수정
# print(g)
# g.update((("미국","워싱턴 D.C"),("이집트","카이로"))) # 튜플로 수정
# print(g)
# print(g.pop("미국")) # 해당키 삭제하고 값 리턴 * 키가 없으면 None 또는 두번째 인자 리턴
# print(g)
# print(g.popitem()) # 마지막 쌍 삭제 후 튜플로 리턴
# print(g)
# g.clear() # 모든 값 삭제
# print(g)
# print("-----------------")

# print(g.keys()) # 키(key)로 리스트 만들기 *dict_keys
# print(g.values()) # 값(value)으로 리스트 만들기 *dict_values
# print(g.items()) # 키(key), 값(value) 한쌍의 튜플로 리스트 만들기 *dict_items
# print(list(g.keys()))
# print(list(g.values()))
# print(list(g.items()))
# print("-----------------")

# a = ['a', 'b', 'c', 'd']
# b = dict.fromkeys(a, "값없음") # 리스트(튜플)로 딕셔너리 만들기 * 두번째 인자가 없으면 값으로 None
# print(b)

# c = [[1,2],[3,4],[5,6]]
# d = dict(c)
# print(d)

# if "대한민국" in g: # 키로 연산
#     print("키가 있다")
# else:
#     print("키가 없다")

# for i in g: # 키로 반복
#     print(i)

# 정수, 실수, 복소수, 문자열, 리스트[], 튜플(), 딕셔너리{'1':'일'}, 세트, 불