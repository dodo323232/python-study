def calc(r1):
    result = 3.14 * r1 ** 2  # r1 : 반지
    return result
r = int(input("원의 반지름 입력:"))
area=calc(r)
print("원의 넓이:", area)