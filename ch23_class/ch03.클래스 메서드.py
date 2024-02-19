import datetime
class Lotto:
    cnt = 0
    datetimeFormat = "%Y/%m(%B)/%d(%a) %H:%M:%S"
    
    def __init__(self):
        self.number = []
        Lotto.cnt += 1
        self.turningTrain = Lotto.cnt
        self.selectDatetime = datetime.datetime.now()
    
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
        print(f"{self.turningTrain}회차 당첨번호 : {self.number} 추첨시간 : {self.selectDatetime.strftime(Lotto.datetimeFormat)}")

    # @classmethod
    # def changeDatetimeFormat(cls, datetimeFormat):
    #     cls.datetimeFormat = datetimeFormat

lotto1 = Lotto()
lotto1.numberSelect()
lotto2 = Lotto()
lotto2.numberSelect()
lotto1.allPrint()
lotto2.allPrint()

# print('-' * 30)
# Lotto.changeDatetimeFormat("%Y년%m(%B)월%d(%a)일 %H:%M:%S")
# lotto1.allPrint()
# lotto2.allPrint()