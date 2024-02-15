# (랜럼숫자리턴함수)1~45까지의 랜던 숫자 6개를 리턴 해주는 함수를 만드시오
# return은 리스트   # random.randint(1, 45)
import random 
def random_num():
    random_list = []
    for i in range(0, 6):
        num = random.randint(1, 45)
        random_list.append(num)
    return random_list
print(random_num())

# (랜럼숫자리턴함수-중복x)1~45까지의 랜던 숫자 6개를 리턴 해주는 함수를 만드시오
# return은 리스트   # random.randint(1, 45)
# import random 
# def random_num():
#     random_list = set()
#     while True:
#         num = random.randint(1, 45)
#         random_list.add(num)
#         if len(random_list) == 6:
#             break
#     return list(random_list)
# print(random_num())