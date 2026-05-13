def calc(r1):
    result = 3.14 * r1 ** 2
    return result

r=float(input("원의 반지름 입력: "))
print("원의 넓이:", calc(r))
# print(result) # 함수 안에서 선언된 변수는 함수 밖에서 사용할 수 없다. (지역변수)

######################################################################################

def calc(r2):
    global a # 전역 변수 a를 사용하겠다는 선언
    a = 3.14 * r2 ** 2
    return a # 지역 변수
a=0 # 전역 변수
rr=float(input("원의 반지름 입력: "))
print("원의 넓이:", calc(rr))
print(a) # 함수 안에서 선언된 변수는 함수 밖에서 사용할 수 없다. (지역변수)

