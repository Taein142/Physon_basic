# 보기 Person클래스는 사람 한명을 표현하고, 이름(str), 나이(int), 결혼유무(bool)를 나타낼 수 있다.

# 요구 사항
# 보기의 Person 클래스를 객체로 두개 생성하시오.
# 생성한 두 개의 Person 객체를 아래와 같이 ageUp, marriage 메서드로 값을 변경하고 Person 클래스의 print메서드로 출력하시오.
# ageUp메서드로 나이를 1증가 시키시오
# marriage메서드로 결혼여부를 변경하시오
# print메서드로 전체 데이터를 출력하시오
# 수준별 요구 사항
# 난이도 중) ageUp메서드 변경
# 매개변수: 숫자 하나
# 실행문구:  받은 매개변수만큼 나이를 올리시오
# 난이도 상) marriage메서드 변경
# 매개변수: 없음
# 현재 결혼상태를 반대로 돌리시오
# 보기 : 파일로도 첨부되어 있음.

class Person:
    def __init__(self, name, age, married):
        self.name = name
        self.age = age
        self.married = married
    
    def ageUp(self):
        self.age += 1

    def marriage(self, status):
        self.married = status

    def print(self):
        print(f"{self.name}\t{self.age}\t{self.married}")

person1 = Person("김가나", 20, True)
person2 = Person("박다라", 25, False)

person1.ageUp()
person2.ageUp()

person1.marriage(False)
person2.marriage(True)

person1.print()
person2.print()