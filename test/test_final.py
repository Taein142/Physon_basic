# ▶ 회원(User) 클래스 만들기

# 요구 사항
# 인스턴스 변수 : 회원이름(name), 회원아이디(id), 회원비밀번호(password), 가입날짜(joindate)
# 생성자 만들기
# 난이도 하) 인스턴스 변수 name, id, password, joindate를 매개변수로 받아 대입하시오
# 난이도 중) 인스턴스 변수 joindate는 datetime모듈을 활용하여 현재 날짜를 자동으로 대입하시오 **date클래스에서 today()메서드 사용
# 메서드 만들기
# 모든 인스턴스 변수를 출력하는 메서드를 만드시오
# 출력 함수는 print()를 사용하시오

# 회원(User) 클래스 만들기 - 한명의 회원은 하나의 User클래스 객체이다

from datetime import date

class User:
    def __init__(self, name, id, password, joindate=None):
        self.name = name
        self.id = id
        self.password = password
        self.joindate = joindate if joindate is not None else date.today()

    def print(self):
        print(f"{self.name}\t{self.id}\t{self.password}\t{self.joindate}")

user1 = User(name="김매미", id="맴맴맴맴매애애앰", password=1234)
user1.print()


# ▶  회원(User) 클래스를 활용하여 회원가입/로그인 프로그램 완성하기

# 요구 사항
# 반복하면서 메뉴를 입력 받아 프로그램을 실행하시오.(첨부 파일 참고)
# 회원가입
# 데이터를 입력 받으시오
# 입력 받은 데이터로 User객체를 생성하시오
# 생성한 객체를 userList에 담으시오 
# 난이도 상) 아이디 중복 체크를 하시오 ** 중복 체크 함수를 만들어 사용(권장)
# 로그인
# 로그인할 아이디, 로그인할 비밀번호를 입력 받으시오
# userList에 담겨있는 User객체 중에 아이디와 비밀번호가 같은 객체가 있는지 확인하시오
# 아이디, 비밀번호가 일치하는 객체가 있으면 "로그인 성공"을 출력하시오
# 아이디, 비밀번호가 일치하는 객체가 없으면 "로그인 실패"를 출력하시오
# * "로그인 실패"를 출력할 때 여러 번 출력 되지 않게 하시오
# 회원가입 리스트
# userList에 담겨있는 모든 객체의 이름, 아이디, 비밀번호, 가입 날짜를 메서드로 출력하시오
# 종료
# 반복문을 빠져나가시오


# 아이디 중복체크 함수
def idOverlapping(check_id):
    for user in userList:
        if user.id == id:
            return True
    return False

# 회원(User) 클래스를 활용하여 회원가입/로그인 프로그램 완성하기
userList = [] # 회원가입한 회원 저장소

while True:
    print("===================================")
    print("1.회원가입 2.로그인 3.리스트 0.종료")
    print("===================================")
    menu = input("메뉴입력> ")

    if menu == "1":
        # 이름, 아이디, 비밀번호 입력 받아서 User객체 생성 후 userList에 저장하기
        name = input("이름를 입력하세요: ")
        id = input("아이디를 입력하세요: ")

        while idOverlapping(id):
            print("사용중인 아이디입니다.")
            id = input("아이디를 입력하세요: ")

        password = input("비밀번호를 입력하세요: ")

        user = User(name=name, id=id, password=password)
        userList.append(user)
        print("회원가입 완료되었습니다.")

    elif menu == "2":
        # 로그인할 아이디와 비밀번호 받아서 "로그인 성공" 또는 "로그인 실패" 출력하기
        id = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        login_check = False
        for user in userList:
            if user.id == id and user.password == password:
                login_check = True
                break
        
        if login_check:
            print("로그인 성공")
        else:
            print("로그인 실패")

    elif menu== "3":
        # 모든 유저의 이름, 아이디, 비밀번호, 가입날짜 출력하기
        for user in userList:
            user.print()

    elif menu == "0":
        # 반복문 빠져나가기
        break

    else:
        print("0~3까지 입력가능")
    print()

print("프로그램이 종료되었습니다")