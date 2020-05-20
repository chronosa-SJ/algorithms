NUMBER, M = list(map(int, input().split()))
#print(NUMBER, M)

str_num = list(str(NUMBER))

remove_cnt = 0
stack = [str_num[0]]
for i in range(1, len(str_num)):
    while len(stack) > 0 and remove_cnt < M:
        #print(str_num[i], stack)
        if str_num[i] > stack[-1]:
            stack.pop()
            remove_cnt += 1
        else:
            break
    stack.append(str_num[i])

for i in range(M-remove_cnt):
    stack.pop()

print(''.join(stack))
