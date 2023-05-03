from collections import deque

def solve(x,y):
    global cnt
    q = deque([])
    if visited[x][y] == 0:
        q.append([x, y])
        cnt += 1
        visited[x][y] = cnt
        ans.append(1)
    while q:
        r, c = q.popleft()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = r+d[0], c+d[1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[r][c]
                ans[cnt] += 1
                q.append([nx,ny])

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
ans = [0]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            solve(i,j)
ans.sort()
ans[0] = len(ans)-1
for i in ans:
    print(i)