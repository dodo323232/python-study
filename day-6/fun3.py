def dis_price(a,b):
    return a - (a//b)


# a상품: 10000원 할인율: 10
price_a=dis_price(10000,10) #dis_price 함수명
print(price_a) # 할인금액을 뺀 금액

price_a=dis_price(50000,20)
print(price_a)# 할인금액을 뺸 금액이다