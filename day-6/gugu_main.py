# from gugu_modul import *
# b=True
# while b:
#     a=int(input("1: 세로형 | 2: 가로형 | 0: 종료 : "))
#     match a:
#         case 1: v_gugudan()
#         case 2: h_gugudan()
#         case 0: b=False
#         case _: 
#             print("잘못 입력")
#             continue
from gugu_modul import *

r = 1
while r:
    num = int(input("\n숫자를 선택하세요(1: 세로 구구단   |||   2: 가로 구구단   |||   0: 종료): \n"))
    if num == 1:
        v_gugudan()

    elif num == 2:
        h_gugudan()

    elif num == 0:
        print("\n프로그램이 종료되었습니다.")
        r = 0
        
    else:
        print("\n잘못된 입력입니다.")
