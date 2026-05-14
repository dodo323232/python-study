try: # 수행 문장 안에 예외 발생하면.. | except: 예외 발생시 출력
    num=int(input("숫자 입력"))
    res=10/num
except ValueError: # 값 오류
    print("숫자가 아닙니다.")
except ZeroDivisionError: # 0으로 나눌때
    print("0으로 나눌 수 없다.")
except  Exception as e: # 그 외 나머지 예외인 경우 -> e 예외 저장
    print("에러메세지",e)
else: # 정상적인 경우
    print("결과:",res)
finally: # 공통적 수행 (무조건 수행)
    print("종료")