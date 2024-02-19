class Lotto:
    cnt = 0
    
    def __init__(self):
        self.number = []
        Lotto.cnt += 1 # 인스턴스변수 접근 예) lotto1.number
        self.turningTrain = Lotto.cnt
    
    def numberSelect(self):
        import random
        numbers = set()
        while True:
            number = random.randint(1, 45)
            numbers.add(number)
            if len(numbers) == 6:
                break
        self.number.extend(list(numbers))
    
    def allPrint(self):
        print(f"{self.turningTrain}회차 당첨번호 : {self.number}")

lotto1 = Lotto()
lotto1.numberSelect()
lotto2 = Lotto()
lotto2.numberSelect()

lotto1.allPrint()
lotto2.allPrint()

# print(Lotto.cnt)
# print(lotto1.cnt)
# print(lotto2.cnt)
# print('-' * 30)

# Lotto.cnt += 1
# print(lotto1.cnt)
# print(lotto2.cnt)
# print('-' * 30)

# 주의사항
# lotto1.cnt += 1 
# print(lotto1.cnt)
# print(lotto2.cnt)