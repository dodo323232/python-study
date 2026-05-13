res = divmod(11,3)
print("divmod(11,3):", res) # 3,2 몫(//), 나머지(%)
print("abs(-5):", abs(-5)) #절대값
print("pow(4,2):", pow(4,2)) # 4의 2제곱
print("최댓값:", max(10,30,5)) #최댓값 
print("최솟값:", min(10,30,5)) #최솟값
print("round(23.89):", round(23.89)) #소수점 2자리까지 반올림


import math  # math 모듈 (내장함수) | math.함수명()으로 사용해야만 한다
#from math import * # math 모듈의 모든 함수 사용 가능 | math.함수명()으로 사용하지 않아도 된다    

#내림
print("floor(24.9):", math.floor(24.9)) #소수점 2자리까지 내림s
#올림 
print("ceil(23.8):", math.ceil(23.8)) #소수점 2자리까지 올림
print("sqrt(16):", math.sqrt(16)) #제곱근
print("factorial(5):", math.factorial(5)) #팩토리얼  
print("math.pi:", math.pi) #원주율