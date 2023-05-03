N, K = map(int, input().split())
lis = list(map(int, input().split()))
maxN = max(lis)
cnt_lis = [0]*(maxN+1)
l, r, ans = 0, 0, 0              # 투포인터 문제 l = > left, r => right
while r < N:                     # cnt_lis 에 해당 수열의 value 를 담으면서 카운트
    if cnt_lis[lis[r]] < K:      # 카운트가 K 개보다 적으면 카운팅하며 r  증가
        cnt_lis[lis[r]] += 1
        r += 1
    else:                        # 카운트가 K개가 이미 되었다면 cnt 1 빼주고 l 증가
        cnt_lis[lis[l]] -= 1
        l += 1
    ans = max(ans, r - l)
print(ans)


# 예시 : 3 2 5 5 6 4 4 5 7