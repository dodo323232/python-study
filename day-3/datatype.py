#리스트
subway=["아이유","변우석","박지훈","유재석"]
print(subway)

subway.append("장원영") #추가
print(subway)

subway.insert(1,"카리나")
print(subway)

print(subway.index("박지훈")) #위치

print(subway.pop()) #뒤 자료 삭제

print(subway)

name=subway.pop(1) #1번째 삭제된 값을 반환 | 리스트 번호를 입력
print(name)

subway.remove("유재석") #값 삭제
print(subway)

subway.append("아이유")
print(subway)

print(subway.count("아이유"))

subway.remove("아이유") #리스트 안에 값을 입력
print(subway)

num_list=[2,4,5,1,3]
print(num_list)

num_list.sort()
print(num_list) #오름차순 정렬(작->큰)

num_list.reverse() #내림차순 정렬
print(num_list)

num_list.clear() #리스트 전체 삭제
print(num_list)

#튜플 : 순서 있음, 나열형, 변경 불가
menu=("김밥","오뎅")
print(menu)
# menu[1]="피자"
print(menu)

(name,age,addr) = ("이순신",30,"안산")
print(name,age,addr)

#딕셔너리 : 키와 값 쌍으로 구성
classroom={407:"개발자과정", 402:"영상과정"}
print(classroom)
print(classroom[407]) #하나하나의 요소를 나타낼 때는 대괄호
# print(classroom[404]) #오류

print(classroom.get(407))
print(classroom.get(404))

print(classroom.keys()) # 키 
print(classroom.values()) # 값
print(classroom.items()) # 키:값

del classroom[402]
#del-> 전반적인 통용되는삭제
print(classroom)