# 디폴트 인수 : 함수의 매개변수가 기본값을 갖고 있을 수 있음
def greet(name,msg="별일없지?"):
    print(f"안녕 {name}, {msg}")

greet("홍길동")

###################################

def print_star(n=1): # 인수 값이 호출할때 간다면 그 값이 먼저
    # 인수값이 없을때만 디플토인수
    print("n=",n)
    for i in range(n):
        print("***************")
print_star() #인수가 없음
print_star(3) #인수를 3을 보내면서 호출