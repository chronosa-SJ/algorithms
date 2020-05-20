sys.stdin = open("in2.txt", "rt")

N = int(input())
meeting_rooms = []
for _ in range(N):
    meeting_rooms.append(tuple(map(int, input().split())))
meeting_rooms.sort(key=lambda x: (x[1], x[0]))
print(meeting_rooms)

start_time = 0
end_time = meeting_rooms[0][1]
cnt = 1

for i in range(1, N):
    start_time = meeting_rooms[i][0]
    if start_time >= end_time:
        end_time = meeting_rooms[i][1]
        cnt += 1

print(cnt)
