import sys
from pprint import pprint

sys.stdin=open("in1.txt", "rt")
N = int(input())

arr = []
arr.append([0 for _ in range(N+2)])
for _ in range(N):
    input_list = list(map(int, input().split()))
    input_list.insert(0, 0)
    input_list.append(0)
    arr.append(input_list)
arr.append([0 for _ in range(N+2)])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

bong_map =[[1 for _ in range(N+2)] for _ in range(N+2)]
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if bong_map[i][j] == 0:
            continue

        now = arr[i][j]
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
            bong_map[i+1][j] = bong_map[i][j+1] = bong_map[i][j-1] = 0

print(cnt)
