# 함수
def add(n,m):  # () 안에는 매개변수
    return n+m

n1=int(input("숫자1 입력 : "))
n2=int(input("숫자2 입력 : "))

sum1 = add(n1,n2) # 함수 호출(인수), 리턴값을 저장

print(sum1)

# sum(): 합계
# len(): 길이
# 숫자 리스트의 평균을 반환
def avg(score_list):
    if not score_list:      #예외 처리문
        return 0
    return sum(score_list)/len(score_list)
score_list=[80,90,100,50,70]

print(avg(score_list))