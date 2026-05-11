# for i in range(6)
# =>0~5 6번 반복
# 딕셔너리 : 키+값
snack={
    "새우깡": 300,
    "매운 새우깡": 3500,   # 딕셔너리 쓴 대로 출력됨
    "양파링": 4000
    }
for i in snack: # 꼭 range 안 써도 됨
    print(i) # 키 값만 출력
print()
for j in snack.items(): # key값과 value 출력
    print(j)
print()
for j in snack.keys(): # key값 출력
    print(j)
print()
for j in snack.values(): # value 출력
    print(j)
print()

#리스트
fruit=["파인애플","참외","배","오렌지","골든키위"]
cart=[]
for i in fruit:
    print(i)
    if len(i)<=3:
        cart.append(i)
print(cart)