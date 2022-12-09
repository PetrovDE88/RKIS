nums = (2, 7, 11, 15, 21)
target = 28
for i in range(len(nums) - 1):
    if (target - nums[i]) in nums[i + 1:]:
        print(f'[{i}, {nums.index(target - nums[i])}]')
