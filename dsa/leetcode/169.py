# O(n) time | O(1) space
def majorityElement(nums):
    ans = -1 
    count = 0

    for num in nums:
        if count == 0:
            ans = num
        
        if ans == num:
            count += 1
        else:
            count -= 1
    return ans

nums = [3,2,3]
print(majorityElement(nums))
