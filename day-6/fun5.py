# *args: "arguments"의 약자로, 함수에 전달되는 위치 인수들을 튜플로 받아들이는 매개변수입니다.
# **kwargs: "keyword arguments"의 약자로, 함수에 전달되는 키워드 인수들을 딕셔너리로 받아들이는 매개변수입니다.

def manyParam(*args):
    # 몇개의 매개변수를 받을지 모를 때는 변수 앞에 '*'를 붙여준다.
    print(type(args)) # 튜플로 저장
    sum = 0
    for i in args:
        sum += i
    return sum

print(manyParam(1,2,3,4,5,6,7,8,9,10)) # 55
print(manyParam(1,2,3,4,5)) # 15
print('-'*30)

def dictParam(**kwargs):
    # 몇개의 매개변수를 받을지 모를 때는 변수 앞에 '**'를 붙여준다.
    print(kwargs) # 딕셔너리로 저장
    
dictParam(a="A") # {'a': 'A'}
dictParam(x=10,y=20,z=30)  # {'x': 10, 'y': 20, 'z': 30}
print("-"*30)
#이름이 있는 여러개의 값을 받을 떄 사용하는 문법
