import sys
sys.stdin = open('input.txt', 'r')

def binary_search(trees, s, e):
    res = 0
    while s <= e:
        m = (s+e)//2
        cnt = 0

        for tree in trees:
            if tree > m:
                cnt += tree-m

        if cnt < M:
            e = m - 1
        else:
            res = m
            s = m + 1

    return res

N, M = map(int, input().split())
trees = list(map(int, input().split()))
ans = binary_search(trees, 0, max(trees))
print(ans)