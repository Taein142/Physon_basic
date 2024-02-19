class Lotto:
    def __init__(self):
        self.number = []
    
    def numberSelect(self):
        import random
        numbers = set()
        while True:
            number = random.randint(1, 45)
            numbers.add(number)
            if len(numbers) == 6:
                break
        self.number.extend(list(numbers))

lotto1 = Lotto()
lotto1.numberSelect()
print(lotto1.number)

lotto2 = Lotto()
lotto2.numberSelect()
print(lotto2.number)