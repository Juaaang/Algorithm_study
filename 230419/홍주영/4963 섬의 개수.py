from collections import deque

def solve(x,y):
    global cnt
    q = deque([])
    if visited[x][y] == 0:
        q.append([x, y])         #섬마다 다른 번호로 입혀줌
        cnt += 1
        visited[x][y] = cnt
    while q:
        r, c = q.popleft()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = r+d[0], c+d[1]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[r][c]
                q.append([nx,ny])

# 다 돈다는 뜻
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                solve(i,j)       #그룹핑 시작
    print(cnt)