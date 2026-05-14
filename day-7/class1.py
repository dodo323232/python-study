class Board:
    def set_data(self,title,writer): # 책제목, 저자 저장
        self.title = title # self는 자바처럼 this의 역할도 하고, 객체를 대입하는 역할
                           # 왼쪽 title은 객체(붕어빵)의 맴버변수
                           # 내자신(객체)의미:self
        self.writer = writer
        self.cnt = 0
    
    def cntup(self): # 조회수를 구하는 함수
        self.cnt +=1
# 게시판 객체 생성
#   Board b1 = new Board() 자바
board1 = Board() # 객체 변수=클래스(매개변수)
board2 = Board()

board1.set_data("자바의 정석","홍길동")
board2.set_data("파이썬의 정석","이순신")
board1.cntup()
board1.cntup()
board2.cntup()
print(board1.title,board1.writer,board1.cnt)
print(board2.title,board2.writer,board2.cnt)

board3= Board()
# boatd3.cntup()  오류 set_data를 부르지 않았기 때문에 cnt가 0을 받지 못했다
