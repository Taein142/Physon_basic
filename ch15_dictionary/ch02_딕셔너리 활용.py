# 딕셔너리 활용
car = {"name":"그랜져", "color":"검정", "maxspeed":300}
car["sunroof"] = True # 추가
car.setdefault("sunroof", False) # 있으면 추가,수정 안함

if "color" in car: # 키로 연산
    car["color"] = "빨강" # 수정
    car.update(color = "빨강")
print(car)
print("-----------------")

# print(car.keys())
# for i in car: # 키로 반복 car.keys()
#     print(i)
# print("-----------------")

# print(car.values())
# for i in car.values(): # 값으로 반복
#     print(i)
# print("-----------------")

# print(car.items())
# for i, j in car.items(): # 키/값 쌍으로 반복
#     print(f"key : {i} 	 value : {j}")
# print("-----------------")