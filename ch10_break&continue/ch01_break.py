# break
for i in range(0, 10):
    print(i)
    if(i == 4):
        break
    
while True:
    a = input("종료입력하면 종료됩니다> ")
    if a == "종료":
        break
print("종료되었습니다")
"""실행시 입력 인자값을 아래와 같이 넣은 후 실행해주세요.
1
2
종료
"""