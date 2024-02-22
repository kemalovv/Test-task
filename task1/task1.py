n, m = map(int, input().split())
cur_num = 1
ans = [1]

while True:
    for i in range(m - 1):
        if cur_num + 1 > n:
            cur_num = 1
        else:
            cur_num += 1

    if cur_num == 1:
        break
    else:
        ans.append(cur_num)

print("".join(str(j) for j in ans))
