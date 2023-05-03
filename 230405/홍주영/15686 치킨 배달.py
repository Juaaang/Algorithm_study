import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):                                      # 집과 치킨가게의 위치의 좌표를 list에 추가
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i,j])
        if arr[i][j] == 2:
            chicken.append([i,j])
select_chic = list(combinations(chicken, M))         # 문제에서 요구하는 M개 만큼의 치킨집을 조합을 통해 가져옴
print(select_chic)
ans = 10000
i = 0
while i < len(select_chic):
    sumD = 0  # 1번 수행했을 때 거리의 합
    for idx in house:
        tmp = 100       # 최대거리
        for c in range(M):
            if abs(select_chic[i][c][0]-idx[0]) + abs(select_chic[i][c][1] - idx[1]) < tmp: # 좌표계싼
                tmp = abs(select_chic[i][c][0]-idx[0]) + abs(select_chic[i][c][1] - idx[1])
        sumD += tmp
    if sumD < ans:
        ans = sumD      # ans 보다 작으면 ans 에 sumD를 넣어주고
    i += 1              # 조합 select_chic 반복

print(ans)