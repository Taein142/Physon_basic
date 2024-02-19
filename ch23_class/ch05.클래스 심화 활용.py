class 롯데선물세트:
    trademark = '롯데'
    
    def __init__(self, can, oil, sauce, ham = None):
        self.can = can
        self.oil = oil
        self.sauce = sauce
        self.ham = ham
        self.allPrint()

    def allPrint(self):
        print(f"**{롯데선물세트.trademark}종합선물세트**\n1.{self.can}	2.{self.oil}	3.{self.sauce}	{'4.'+self.ham if self.ham!=None else ''}")
    
    @classmethod
    def trademarkCompany(cls, trademark):
        cls.trademark = trademark
    
참치선물세트 = 롯데선물세트('참치캔', '해바라기유', '진간장')
연어선물세트 = 롯데선물세트('연어캔', '올리브유', '국간장')
프리미엄참치선물세트 = 롯데선물세트('참치캔', '까놀라유', '진간장', '스팸')
프리미엄연어선물세트 = 롯데선물세트('연어캔', '올리브유', '양조간장', '리챔')
print('-' * 30)

# 롯데선물세트.trademarkCompany('LOTTE')
# 참치선물세트.allPrint()
# 연어선물세트.allPrint()
# 프리미엄참치선물세트.allPrint()
# 프리미엄연어선물세트.allPrint()