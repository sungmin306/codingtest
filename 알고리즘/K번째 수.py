t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    L = list(map(int, input().split())) # 리스트에 한줄로 읽고 쓰는 방법
    L= L[s-1:e ] # 슬라이스를 이용해서 s-1 부터 e바로전번째 까지만 slice 
    L.sort() # 오름차순 정렬
    print("#{0} {1}".format(i, L[k-1]))