"""
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
def general(nums):
        result = []
        cnt = 0

        for k in range(len(nums)):
            if nums[k] != 0:
                result.append(nums[k])
            else:
                cnt += 1
        for i in range(cnt):
            result.append("0")
        return result

#now "modifying nums in place"
def inplace(nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                 nums[i], nums[j] = nums[j], nums[i]
                 j += 1
        return nums

#here we are using unecessary swaps 
def inplace_without_swap(nums):
     j = 0
     for i in range(len(nums)):
          if nums[i] != 0:
               nums[j] = nums[i]
               j += 1
     for k in range(j, len(nums)):
          nums[k] = 0
     return print(nums)



nums = [0, 1, 0, 3, 12]
inplace_without_swap(nums)
