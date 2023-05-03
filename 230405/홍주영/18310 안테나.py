'''
결국 중앙값에 안테나를 세워야 목표값이 가장 작음
집이 겹쳐도 결국에 house라는 list 값의 중앙값을 가져오는 것이므로
결론은 중앙에 설치 했을 때 가장 짧은 값이 나옴
'''


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(N-1)//2])


