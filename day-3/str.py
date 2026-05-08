# 문자열
s="Hello Python"
print(s[6]) # 인덱싱
#print(s[6:])
print(s[6:12]) # 슬라이싱

jumin="080430-3133445"
print("성별:",jumin[7])
print("월:",jumin[2:4]) # 2~3
print("일:",jumin[4:6]) # 4~5
#print("뒷자리:",jumin[7:]) # 7~끝까지
print("뒷자리:",jumin[-7:]) # -7~끝까지    기억해두기

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3='재미있습니다'  #파이썬은 따옴표 구별 안함
s4="""                  #여러문자열 저장할때, 입력한 그대로 저장
나는 학생입니다
파이썬을 배웁니다
재미있습니다
"""
print(s4)

year="1980"
month="05"
day="23"
date=year+"-"+month+"-"+day
print(date)

date2=date.split("-")
print(date2)
                    #split으로 쪼개지면 리스트 형식으로 들어간다람쥐
print(type(date2))
print(date2[1])
print(date2[1][0:2], end="*")   #end는 맨 뒤에 문자 붙인다  |  줄바꿈 방지 및 '*'로 구분

name="kakao taxi"
name2=name.replace("k","t",1) #앞이 바뀔 문자, 뒤가 빠구는 문자, 숫자는 몇개 할지
#replace : 변경
print()
print(name2)

print("python"*5) # 문자열 곱하기는 반복의 뜻

won="63,120,450"
won2=won.replace(","," ")
print(won2)

won3=345908800
won4=format(won3,",d") # ",d"는 정수 숫자를 세자리 마다 쉼표 입력시키고 문자열로 바꿔라
print(won4)

#문자열 대소문자, 길이
p="Python is Amazing"
print(p.lower()) # 소문자
print(p.upper()) # 대문자
print(p.capitalize()) # 첫글자 대문자
print(p[0].isupper()) # true
print(len(p)) # 길이
print(p.count("i")) # 개수

#위치
index=p.index("i") #7
print(index)
index=p.index("i",index+1) #14
print(index)

#문자열 연결
words = ["Python","is","easy"]
result = " ".join(words) # " " -> 사이에 공백 넣으면서 연결
print(result)

#제거
text= "   Hello     Python****"
print(text.strip())# 공백 제거
print(text.rstrip("*")) # 오른쪽 * 제거, .lstrip():왼쪽부터

#자리수만큼 0으로 채우기
num = "5"
result = num.zfill(3)
print(result)

#format
age=19
print("나는 %d살입니다" %age) #19를 %d 자리에 넣음
print("나는 {}살입니다".format(age))

like="노래부르기"
print("나는 %d살이고 %s를 좋아해요"%(age,like))
print("나는 {0}살이고 {1}를 좋아해요".format(age,like))  # 0에는 age가 들어가고 1에는 like가 들어감

# f 스트링
print((f"나는 {age}살이고 {like}를 좋아해요"))  #기억하셈

print("나의 주소는 {addr}이며, 나의 키는 {height}cm 입니다".format(addr="인천", height=165))

# 이스케이프(탈출) 문자
print("\n배우는 과목은\n \"파이썬\" 입니다")
# \r : 커서를 맨 앞으로 이동
print("red  apple\rpine") # \r은 맨 앞으로 덮어씌우기
print("i like you!\b!!") # \b은 한 글자 삭제
print("red\t   apple") # \t는 탭이동

# 인덱스 찾기
print(p.find("A")) # 왼쪽부터 찾아서 인덱스 번호 출력, 10
print(p.rfind("A")) # 오른쪽 부터
print(p.index("a")) # 왼쪽부터 찾아서 인덱스 번호 출력, 12
print(p.rindex("a")) # 오른쪽 부터

print(p.find("java")) # 없는 문자를 찾으면 -1
# print(p.index("java")) # 없는 문자를 찾으면 에러 발생

arr_Str=input("Input String : ").split("-") # information-technology
# information-technology -> "-"기준으로 조갬[0][1] 나누어서
arr_Len=int(input("Input Number : "))# 12 
arr_Val=list(range(0,arr_Len,2)) # 0 2 4 6 8 10 
arr_Val.remove(4)# 4라는 값을 삭제 -> 0 2 6 8 10
print(arr_Str[1].find("i")+arr_Val[2]) # -1 + 6 = 5