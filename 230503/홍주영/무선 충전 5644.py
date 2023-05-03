direc = {
    0: [0, 0],
    1: [0, -1],
    2: [1, 0],
    3: [0, 1],
    4: [-1, 0],
}

for tc in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    A_lis = list(map(int, input().split()))
    B_lis = list(map(int, input().split()))
    board = []
    for _ in range(A):
        board.append(list(map(int, input().split())))
    sa = [1, 1]
    sb = [10, 10]

    ans = 0

    a_max = 0
    b_max = 0
    for c in board:
        if abs(sa[0] - c[0]) + abs(sa[1] - c[1]) <= c[2]:
            if a_max < c[3]:
                a_max = c[3]
        if abs(sb[0] - c[0]) + abs(sb[1] - c[1]) <= c[2]:
            if b_max < c[3]:
                b_max = c[3]
    ans += a_max + b_max
    for t in range(M):
        a_dir = A_lis[t]
        sa[0] += direc[a_dir][0]
        sa[1] += direc[a_dir][1]

        b_dir = B_lis[t]
        sb[0] += direc[b_dir][0]
        sb[1] += direc[b_dir][1]

        a_c = []
        b_c = []

        for c in board:
            if abs(sa[0] - c[0]) + abs(sa[1] - c[1]) <= c[2]:
                a_c.append(c)
            if abs(sb[0] - c[0]) + abs(sb[1] - c[1]) <= c[2]:
                b_c.append(c)

        max_sum = 0
        if not len(a_c) and len(b_c):
            for b_cand in b_c:
                if max_sum < b_cand[3]:
                    max_sum = b_cand[3]
        elif len(a_c) and not len(b_c):
            for a_cand in a_c:
                if max_sum < a_cand[3]:
                    max_sum = a_cand[3]
        elif len(a_c) and len(b_c):
            for a_cand in a_c:
                for b_cand in b_c:
                    if a_cand == b_cand:
                        if max_sum < a_cand[3]:
                            max_sum = a_cand[3]
                    else:
                        if max_sum < a_cand[3] + b_cand[3]:
                            max_sum = a_cand[3] + b_cand[3]
        ans += max_sum
    print(f'#{tc}', ans)