# 재귀 호출(함수)(함수 내부에서 자기자신을 호출)
# 5!(팩토리얼) = 5*4*3*2*1
def fact(n): #fact:함수명(매개변수는 1개)
    if n==1:
        return 1 # n이 1이면 1을 반환
    else:
        return n*fact(n-1) # n이 1이 아니면 n*fact(n-1)을 반환 (재귀 호출)

a=int(input("정수를 입력하세요 : ")) #예) 5 입력
res = fact(a) # 함수 호출, 인수 a(정수) 보냄
# 반환되어서 온 결과 값을 res에 저장
print(a,"! =",res,"이다.") # 예) 5! = 120

# 순환(재귀)함수를 활용하여 1부터 입력받은ㅇd
# 숫자까지 합을 구하는 프로그램을 작성하시오.
def factory(n):
    if n==1:
        return 1
    else:
        return n+factory(n-1)

num=int(input("숫자 입력해 : "))
print(f"1부터 {num}까지의 합은 {factory(num)}이다.")