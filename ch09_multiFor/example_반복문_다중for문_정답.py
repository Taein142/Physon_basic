# (별짓기) 다중for문으로 아래 예시와 같이 출력하시오
# 출력 예시
#   *
#   **
#   ***
#   ****
#   *****
for i in range(1, 6):
    for j in range(0, i):
        print("*", end="")
    print()

# (별짓기) 다중for문으로 아래 예시와 같이 출력하시오
# 출력 예시
#   *****
#   ****
#   ***
#   **
#   *
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()