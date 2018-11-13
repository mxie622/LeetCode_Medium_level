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

    return input



# https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                k = i+1
                j = len(nums)-1
                recordOfLast = []
                while k < j:
                    threeSum = nums[i] + nums[k] + nums[j]
                    if threeSum < 0:
                        k += 1
                    elif threeSum > 0:
                        j -= 1
                    else:
                        if nums[j] not in recordOfLast:
                            result.append([nums[i], nums[k], nums[j]])
                            recordOfLast.append(nums[j])
                        k += 1
                        j -= 1
        return result


        return nxt # ugly[-1]





