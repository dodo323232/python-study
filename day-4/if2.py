# jumin=input("주민번호를 입력하세요").split("-")

# if jumin[1][0]=="1" or jumin[1][0]=="3":
#     print("남자")
# elif jumin[1][0]=="2" or jumin[1][0]=="4":
#     print("여자")
# else:
#     print("잘못된 주민번호입니다.")


# jumin = input("주민번호를 입력하세요: ") #080128-3499509
# if jumin[7] == "1" or jumin[7] == "3":
#     print("남성")
# elif jumin[7] == "2" or jumin[7] == "4":
#     print("여성")
# else:
#     print("잘못된 주민번호입니다.")

num = int(input("숫자 입력"))
num2 = int(input("숫자 입력"))
num3 = int(input("숫자 입력"))

if num>num2 and num>num3:
    print("가장 큰 수",num)
elif num2>num and num2>num3:
    print("가장 큰 수",num2)
elif num3>num and num3>num2:
    print("가장 큰 수",num3)