class Board:
    
    def setData(self, title, writer): # 변수 세팅 메서드
        self.title = title
        self.writer = writer
        self.cnt = 0
    
    def cntUp(self): # 조회수 올리기 메서드
        self.cnt += 1

# 게시판 객체 생성
board1 = Board()
board2 = Board()
board1.setData("파이썬은 즐거워", "홍길동")
board2.setData("파이썬이란?", "심청이")

board1.cntUp()
print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)
print('-' * 30)

# board1.cntUp()
# board2.cntUp()
# print(board1.title, board1.writer, board1.cnt)
# print(board2.title, board2.writer, board2.cnt)

# board3 = Board()
# board3.cntUp() # error