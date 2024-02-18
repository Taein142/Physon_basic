class Board:
    
    def __init__(self, title, writer):
        self.title = title
        self.writer = writer
        self.cnt = 0
    
    def cntUp(self):
        self.cnt += 1

board1 = Board("파이썬은 즐거워", "홍길동")
board2 = Board("파이썬이란?", "심청이")

board1.cntUp()
board2.cntUp()
board2.cntUp()

print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)