path = input()
nums = []

with open(path) as f:
    for line in f:
        nums.append(int(line))

nums.sort()
me = nums[len(nums) // 2]
ans = 0

for i in nums:
    ans += abs(me - i)

print(ans)
