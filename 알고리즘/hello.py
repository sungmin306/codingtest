# 2차원 리스트 생성 접근

a = [[0]*3 for _ in range(3)] # -> 2차원 리스트 만들 수 있음

#표처럼 출력하는 방법
for x in a:
    print(x) # x가 의미하는건 행을 의미

# 값만 나오게 하는 방법
for x in a:
    for y in x: # x는 행이므로 y는 행안에 있는 값 즉 list 값이 됨
        print(y, end=' ')
    print()

# 람다 함수(익명의 함수)
plus_two = lambda x: x+2 # 변수에다가 할당을 해줘야함

# 람다 함수 유용한 경우
def plus_one(x):
    return x+1
a = [1,2,3]
#print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a))) #map() 은 함수와 인자 한개씩 매개변수로 받는다.

# 결과 [2,3,4] a 안에 있는 값들을 plus_one 함수인자에 하나씩 넣어줌-> 값이 +1씩 증가함

