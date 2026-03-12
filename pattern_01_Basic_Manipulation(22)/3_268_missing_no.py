#using xor
def missing_no_xor():
    ans = 0
    nums = [3, 0, 1]
    for i in nums:
        ans ^= i
    for i in range(len(nums)):
        ans ^= i
    print(i)

