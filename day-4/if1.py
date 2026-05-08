# eng = input("영어 1글자 입력 : ")

# if eng.isupper : # 대문자 -> true | 아니면 -> false
#     print(eng.lower()) # true일때 수행 -> 소문자
# else :
#     print(eng.upper()) # 대문자로 변경


score=int(input("점수를 입력하세요 : "))
if 80<score<=100:  # 파이썬은 and, or 영어로 씀
    print("A")
elif 60<score:
    print("B")
elif 40<score:
    print("C")
elif 20<score:
    print("D")
elif 0<=score:
    print("E")