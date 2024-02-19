class Lotto:
    def __init__(self, turningTrain):
        self.number = []
        self.turningTrain = turningTrain
    
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

lotto1 = Lotto(1)
lotto1.numberSelect()
lotto1.allPrint()

lotto2 = Lotto(2)
lotto2.numberSelect()
lotto2.allPrint()