

for tc in range(1, int(input())+1):
    N = int(input())
    L = list(map(int, input().split()))
    new_L = [0]*N
    L.sort(reverse=True)
    for i in range(N):
        if i%2:
            new_L[N-(1+(i//2))] = L[i]
        else:
            new_L[i//2] = L[i]
    ans = 0
    for i in range(N-1):
        ans = max(ans, abs(new_L[i]-new_L[i+1]))
    print(ans)