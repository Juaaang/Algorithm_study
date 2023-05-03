# import sys
# sys.stdin = open('input.txt', 'r')

def cal(v1, v2, op):              # 계산하는 식
    if op == ops[0]:
        return v1 + v2
    if op == ops[1]:
        return v1 - v2
    if op == ops[2]:
        return v1 * v2
    if op == ops[3]:
        if (v1 < 0 and v2 > 0) or (v2 < 0 and v1 > 0):
            return -(abs(v1) // abs(v2))
        else:
            return abs(v1) // abs(v2)

def solve(k, curS):                          # dfs
    global minV, maxV

    if k == N-1:
        maxV = max(curS, maxV)
        minV = min(curS, minV)
        return
    for i in range(4):
        if op_lis[i]:
            op_lis[i] -= 1
            solve(k+1, cal(curS, lst[k+1], ops[i])) # 맨앞부터 계산하기 때문
            op_lis[i] += 1

N = int(input())
lst = list(map(int, input().split()))
op_lis = list(map(int, input().split()))
ops = ['+', '-', '*', '/']
maxV = -10**9
minV = 10**9
solve(0, lst[0])
print(maxV)
print(minV)
