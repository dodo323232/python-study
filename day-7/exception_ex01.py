fruits = ["사과","배","오렌지"] # 리스트 0~2
try:
    index=int(input("번호를 입력하세요 (0~2) : "))
    #print(fruits[index]) 
    if index<0 or index>=len(fruits):
        raise IndexError # 강제로 예외를 발생시킴
except IndexError:
    print("없는 인덱스 입니다.")
except ValueError:
    print("숫자를 입력하세요.")
except Exception as e:
    print("에러 메세지",e)
else:   # else는 try가 아무 오류 없을때 실행됨
    print(fruits[index]) # 그러므로 try에 안쓰고 else에만 쓰면 거르지 못해서 오류 뜸
finally:
    print("종료")