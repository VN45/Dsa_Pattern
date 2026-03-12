import math
#here we wants to consider negative numbers also

def max_product(nums):
    if len(nums) <= 3:
        return math.prod(nums)
    nums.sort()
    option1 = nums[-1] * nums[-2] * nums[-3]
    option2 = nums[0] * nums[1] * nums[-1]

    return max(option1, option2)
nums = [-100,-98,-1,2,3,4]

print(max_product(nums))