class Passbook:
    def __init__(self,owner,balance):# 예금주,초기 잔액
        self.owner = owner
        self.balance = balance
        
    def deposit(self,money): # 입금 함수
        self.balance = self.balance + money
        print(f"{money}원 입금 완료")
        print(f"현재 잔액 : {self.balance}")
        print()
    
    # 예) 출금 500, 잔액 3000 => 잔액 부족
    def withdraw(self,money): # 출금 함수
        if self.balance >= money: 
            self.balance = self.balance - money
            print(f"현재 잔액 : {self.balance}")
            print()
        else: 
            print("잔액 부족")
            print()

    def showInfo(self):
        print(f"예금주 : {self.owner} 현재 잔액 : {self.balance}원")
        print()

# 자식 클래스
class MinusPassbook(Passbook): # Passbook으로 상속받음
    #재정의(오버라이딩)
    def withdraw(self,money):
        if self.balance - money >= -1000000:
            self.balance = self.balance - money
            print(f"{money}원 출금 완료")
            print(f"현재 잔액 : {self.balance}")
            print()
        else: 
            print("오지게 많이 쓰셨습니다. (한도 초과)")
            print()
# 예) 출금금액이 50000원 

# 실행

account1 = Passbook("홍길동",100000)
account1.deposit(50000)
account1.showInfo()
account1.withdraw(120000)

account1.withdraw(70000)

account2 = MinusPassbook("김철수",100000)
account2.showInfo()
account2.withdraw(120000) # 자식클래스 호출
account2.withdraw(9000000)