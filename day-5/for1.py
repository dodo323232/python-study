a="봄"
b="여름"
print(a,b, sep="과 ",end=" 끝 ")
print()
# sep: 변수 사이에 들어가는 것을 나타냄
# end: 줄을 바꾸지 않고 옆으로 출력(공백도 가능)

#for i in range(1,100,2) 1~99 2씩 증가
# 구구단에서 원하는 단을 입력받아서 출력
#a=int(input("원하는 단을 입력하세요. : "))

for j in range(2,10):
    print(j,"단")
    for i in range(1,10):
        print(f"{i} x {j} = {j*i}",end="  ")
    print()

print()
import time

for k in range(10,0,-1):# 10~1까지
    print(k)
    time.sleep(1)
print("발사!!")