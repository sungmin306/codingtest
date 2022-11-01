#리스트 생성
# 반복문 돌리면서 나머지가 0인 값을 리스트에 저장
# 리스트 중에서 k-1인덱스 리스트 값 출력
# (추가) 약수 개수의 비교를 위해 cnt1, cnt2 를 사용

n, k= map(int, input().split())
L=[0]
cnt1=0
cnt2=0
for i in range(1,n):
    if n % i == 0:
        cnt1+=1
        L[i].append(i)

for i in range(1,k):
    if n % k == 0:
        cnt2+=1

if cnt1 >= cnt2 :
    print(L[k])
else:
    print(-1)




