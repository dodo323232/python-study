# 숫자 입력 -> 출력 반복, 0을 입력하면 종료
t=True
while t: #True 쓰거나 1 써도 됨
    a=int(input("숫자 입력 : "))
    if a==0:
        t=False
        #break
print("반복문 종료")
print()
print("="*20)
print()

menu=["쫄면","김밥","냉면","오뎅"]
b=input("메뉴 선택 : ")

while b in menu: # in : 안에 속해 있는가?
    # b not in menu : b가 포함되지 않았나?
    print(b)
    b=input("메뉴 선택 : ")
    #while 문장 안에서 반드시 거짓으로 변경되는 문장이 나와야 한다.