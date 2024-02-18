title1 = '파이썬은 즐거워'
writer1 = '홍길동'
cnt1 = 0

title2 = '파이썬이란?'
writer2 = '심청이'
cnt2 = 0

# 조회수 올리기
cnt1 += 1
cnt2 += 1
print(title1, writer1, cnt1)
print(title2, writer2, cnt2)

# 클래스
# class Board:
    
#     def setData(self, title, writer, cnt): # 변수 세팅 메서드
#         self.title = title
#         self.writer = writer
#         self.cnt = cnt
    
#     def cntUp(self): # 조회수 올리기 메서드
#         self.cnt += 1

# # 게시판 객체 생성
# board1 = Board()
# board1.setData("파이썬은 즐거워", "홍길동", 0)
# board2 = Board()
# board2.setData("파이썬이란?", "심청이", 0)

# print(board1.title, board1.writer, board1.cnt)
# print(board2.title, board2.writer, board2.cnt)