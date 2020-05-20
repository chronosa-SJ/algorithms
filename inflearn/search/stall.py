import sys
from pprint import pprint

sys.stdin = open("in2.txt", "rt")

N, C = map(int, input().split())
position_list = []
for _ in range(N):
    position = int(input())
    position_list.append(position)
position_list.sort()

lt = position_list[0]
rt = position_list[-1] + 1
hop = max_len = 0
answer = 0

while lt <= rt:
    hop = (lt+rt) // 2

    fixed = 0
    cnt = 1
    for i in range(1, N):
        if position_list[i] - position_list[fixed] >= hop:
            #print(i, fixed, cnt)
            fixed = i
            cnt += 1

    #print(lt, rt, hop, answer, cnt)
    if cnt >= C:
        lt = hop + 1
        answer = hop
    else:
        rt = hop - 1

print(answer)
