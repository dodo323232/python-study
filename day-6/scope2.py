# 스코프(scope)
# 파이썬은 변수를 찾을때 가까운 영역부터 찾는다.
# LEGB 규칙 (Local -> Enclosing -> Global -> Built-in)
# Local : 현재 함수의 지역변수
# Enclosing : 현재 함수가 중첩된 함수인 경우, 외부 함수의 지역변수
# Global : 현재 모듈의 전역변수
# Built-in : 파이썬이 기본적으로 제공하는 내장 함수나 예외 클래스 등 (print, len, input 등)

a = '홍길동' # 전역 변수(global variable)
b = 99 # 전역 변수(global variable)

def function1():
    a = '이순신' # 지역 변수(local variable) & 중첩 함수 변수
    c = [1 ,2 ,3] # 지역 변수(local variable) & 중첩 함수 변수 
    
    def function2():
        d = (1, 2, 3) # 지역 변수(local variable) & 중첩 함수 변수
        print('Local a =',a)
        print('Local b =',b)
        print('Local c =',c)
        print('Local d =',d) 
        
    
    function2()
    print('Enclosing a =',a) 
    print('Enclosing b =',b)
    print('Enclosing c =',c)
    print('Enclosing d =',d) # function2()에서 선언된 d는 function1()에서 사용할 수 없다. (지역변수)
function1()
print('Global a =',a)
print('Global b =',b)
print('Global c =',c) 
print('Global d =',d) 