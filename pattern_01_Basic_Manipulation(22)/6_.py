"""
Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
"""
from bisect import bisect_left, bisect_right

def brute_approach():
    nums = [-3,-2,-1,0,0,1,2]
    pos = 0
    neg = 0
    for i in nums:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            pass
    print(max(pos, neg))


def binary_search_approach(nums):
    #find first zero index
    first_zero = bisect_left(nums, 0)

    #find first positive after 0
    first_pos = bisect_right(nums, 0)

    neg = first_zero
    pos = len(nums) - first_pos 
    return max(neg, pos)

nums = [-3,-2,-1,0,0,1,2]
print(binary_search_approach(nums))