menu=int(input("3의 배수를 입력하세요. : "))
menu2=int(input("5의 배수를 입력하세요. : "))

match menu%3, menu2%5:
    case 0,0: print("num은 3의 배수 num2는 5의 배수")
    case 0,_: print("num은 3의 배수 num2는 아무숫자")        #파이썬은 switch, caase문이 아니라 match, case문을 쓴다
    case _,0: print("num은 아무숫자 num2는 5의 배수")           
    case _: print("둘다 오류")      # default 대신 case _를 쓴다