# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        nums = []
        for j in s:
            if j not in nums:
                nums.append(j)
            else:
                nums = nums[nums.index(j) + 1:]
                nums.append(j)
            count = max(count, len(nums))
        return count

# https://leetcode.com/problems/sort-colors/description/

def sortColors(nums):

    length = len(nums)
    input = []
    count = []
    for i in range(length):
        if nums[i] == 2:
            input.append(nums[i])
        elif nums[i] == 0:
            input.insert(0, nums[i])
        else:
            count.append(1)
            continue
    for j in range(len(input)):
        if input[j] < input[j+1]:
            input = input[:j+1] + count + input[j+1:]
            break
        # else:
        #     continue
    return input

print(sortColors(nums=nums))
