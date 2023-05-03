'''
2번예제
3 대 3으로 나뉨
스타트팀 -> 1, 2 , 3 이면 S_12 S_13 S_23 과 역을 더해야 함.
비교라서 전부 해봐야 함
'''

import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
nums = [i for i in range(N)]
combi = list(combinations(nums, N//2))

ans = 100000
for i in combi:
    link = []
    start = list(i)
    for j in nums:
        if j not in start:
            link.append(j)

    sumS = sumL = 0
    for k in range(N//2 - 1):
        for l in range(k+1, N//2):
            sumS += arr[start[k]][start[l]] + arr[start[l]][start[k]]
            sumL += arr[link[k]][link[l]] + arr[link[l]][link[k]]

    t_ans = abs(sumS-sumL)
    if t_ans < ans:
        ans = t_ans
print(ans)
