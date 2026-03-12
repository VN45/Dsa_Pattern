"""
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
nums = [0, 1, 0, 3, 12]
result = []
cnt = 0

for k in range(len(nums)):
    if nums[k] != 0:
        result.append(nums[k])
    else:
        cnt += 1
for i in range(cnt):
    result.append("0")
print(result)

