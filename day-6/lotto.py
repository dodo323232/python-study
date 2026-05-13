import random
def get_lotto():
    numbers = [] #비어있는 리스트
    while len(numbers) < 6:
        n=random.randint(1,45)
        if n not in numbers: # 중복되면 안됨
            numbers.append(n) # 뒤에 추가한다s
    return numbers
print(get_lotto())