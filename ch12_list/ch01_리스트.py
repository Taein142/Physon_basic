# 리스트(list)
e = [1,2,3]
ee = ['딸기', '사과', '포도', '바나나', '바나나', '멜론', '키위', '바나나']
print(len(e)) # 길이
print(e[1]) # 인덱싱
print(e[1:]) # 슬라이싱
print(e*3) # 리스트 곱하기
e[1] = 4 # 값 수정
print(e)
del e[2] # 값(변수) 삭제
print(e)
print("-------------------------")

# 주요 함수들
# e.append(5) # 값 마지막에 추가
# print(e)

# e.insert(1, 6) # 값 원하는 인덱스에 삽입
# print(e)

# e.sort() #sort 정렬
# print(e)
# ee.sort()
# print(ee)

# e.reverse() # 값 뒤집기
# print(e)

# ee.remove('딸기') # 값 삭제
# print(ee)

# print(ee.pop(1)) # 해당 인덱스에 있는 값 리턴 후 삭제
# print(ee)

# e.extend([4,5]) # 리스트값 추가하여 확장하기
# print(e)

# e.append([4,5])
# print(e)

# print(ee.count('바나나')) # 값 개수 리턴
# print(ee.index('포도')) # 값 인덱스 위치 리턴

# if '포도' in ee:
#     print("있다")
# else:
#     print("없다")

# for i in ee:
#     print(i)

# 정수, 실수, 복소수, 문자열, 리스트[], 튜플(), 딕셔너리{'1':'일'}, 세트, 불