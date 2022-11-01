#리스트 생성
# 반복문 돌리면서 나머지가 0인 값을 리스트에 저장
# 리스트 중에서 k-1인덱스 리스트 값 출력

from matplotlib.widgets import EllipseSelector


n, k= map(int, input().split())
cnt=0
for i in range(1,n+1):
    if n % i == 0:
        cnt+=1
        if cnt == k:
            print(i)
            break

# if cnt < k: 
#     print(-1)

#python for-else 문법이 존재 break 가 안되면 else 문법 실행하는게 있음
# else:
#     print(-1)
