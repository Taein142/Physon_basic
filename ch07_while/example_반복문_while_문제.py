# '안녕하세요'를 반복문을 통하여 10번 출력하시오
i = 0
while i < 10:
    print("안녕하세요")
    i+=1

# 1~100까지의 합을 while문으로 구하여 출력하시오
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 정수를 반복적으로 입력받으면서 '0보다 큼' 또는 '0보다 작음'을 출력하고 0이 입력되면 반복문을 종료하시오
run = True
while run:
    num = int(input())
    if num > 0:
        print("0보다 큼")
    elif num < 0:
        print("0보다 작음")
    else:
        run = False
print("반복문 종료")


# 정수를 반복적으로 입력받다가 짝수가 5개 입력되면 반복문을 종료하시오
run = True
i = 0
while run:
    num = int(input())
    if num%2==0:
        i +=1
        if i==5:
            run = False
print("끝")
