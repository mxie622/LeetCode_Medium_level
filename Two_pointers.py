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