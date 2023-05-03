direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def solve(s,e,d):
    global ans
    if arr[s][e] == 0:
        arr[s][e] = 2
        ans += 1
    cnt = 1
    for i in range(4):
        flag = False
        nx, ny = s+direc[i][0], e+direc[i][1]
        if 0 <= nx < N and 0<= ny < M and arr[nx][ny] == 0:
            cnt = 0
            while True:
                d = (d+3) % 4
                tx, ty = s+direc[d][0], e+direc[d][1]
                if arr[tx][ty] == 0:
                    flag = True
                    break
            solve(s+direc[d][0], e+direc[d][1], d)
            if flag:
                break
    if cnt and 0 <= s-direc[d][0] < N and 0 <= e-direc[d][1] < M:
        if arr[s-direc[d][0]][e-direc[d][1]] == 1:
            return ans
        elif arr[s-direc[d][0]][e-direc[d][1]] == 2:
            solve(s-direc[d][0], e-direc[d][1], d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
solve(r,c,d)
print(ans)