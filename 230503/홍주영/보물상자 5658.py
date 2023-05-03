import sys
sys.stdin = open('input.txt', 'r')

d = {'0': 0, '1': 1, '2': 2,
     '3': 3, '4': 4, '5': 5,
     '6': 6, '7': 7, '8': 8,
     '9': 9, 'A': 10, 'B': 11,
     'C': 12, 'D': 13, 'E': 14,
     'F': 15
     }

def sixToten(string): # => 16진수를 10진수로 바꿈
    for i in range(0, len(string), (N // 4)): # lis 시작부터 끝까지 4개의 범위로
        tmp = 0
        for j in range((N // 4)): # 주어진 한 변의 갯수만큼 돌면서
            tmp += d[string[i + j]] * 16 ** ((N // 4) - (1 + j)) # 16진수를 10진수로 바꿔줌
        ans.add(tmp) # set()인 add에 저장 (중복 피하기 위함)


for tc in range(1, int(input()) + 1):
    ans = set()
    N, K = map(int, input().split())
    lis = list(map(str, input()))
    sixToten(lis)                         # 처음 Rotate 돌기 전에 값을 ans에 담아줌
    for num in range((N // 4) - 1):
        t = lis.pop()            # 끝자리 빼서
        lis.insert(0, t)         # 앞 자리에 넣어줌
        sixToten(lis)            # 10진수로 바꾼 값을 ans에 담아줌
    ans_lis = list(ans)          # set()이기 때문에 list화 해주고
    ans_lis.sort(reverse=True)   # 정렬해서
    print(f'#{tc}', ans_lis[K - 1]) # K번째 값 출력