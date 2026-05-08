money = int(input("투입한 돈: "))
ob_money = int(input("물건값(100원 단위): "))
if(money>ob_money):
    r = money - ob_money
    d = r//500
    e = (r%500) // 100 
    print("거스름돈:",r)
    print("500원 동전의 개수:",d)
    print("100원 동전의 개수:",e)
else:
    print("금액이 적습니다")