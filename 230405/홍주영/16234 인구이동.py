import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(x, y):
    global cnt, ans
    q = deque([])
    q.append([x,y])
    while q:
        r, c = q.popleft()
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = r+d[0], c+d[1]
            if 0 <= nx < N and 0 <= ny < N and L <= abs(A[r][c] - A[nx][ny]) <= R and visited[nx][ny] == 0:
                if visited[r][c] == 0:
                    curS.append(A[r][c])
                    g_cnt.append(1)
                    cnt += 1
                visited[nx][ny] = visited[r][c] = cnt
                curS[cnt] += A[nx][ny]
                g_cnt[cnt] += 1
                q.append([nx,ny])

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0     # 결과값
while True:
    cnt = 0      # 연합의 갯수
    curS = [0]   # 리스트이 인덱스는 연합 번호의 합
    g_cnt = [0]  # 리스트의 인덱스는 연합 갯수의 합
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i, j)
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                A[i][j] = curS[visited[i][j]] // g_cnt[visited[i][j]]

    if cnt != 0:
        ans += 1
        continue
    elif cnt == 0:
        break
print(ans)


