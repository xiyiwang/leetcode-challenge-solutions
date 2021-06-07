"""
LeetCode Challenge: Longest Consecutive Sequence (2021-06-06)

Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

class Solution:
    # brute force
    def longestConsecutive(self, nums: list) -> int:
        longest_streak = 0
        
        for num in nums:
            curr_num = num
            curr_streak = 1
            
            while curr_num + 1 in nums:
                curr_num += 1
                curr_streak += 1
            
            longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak
    
    # sorting: O(nlgn)
    def longestConsecutive2(self, nums: list) -> int:
        if not nums: return 0
        
        nums.sort()
        
        longest_streak = curr_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    curr_streak += 1
                else:
                    longest_streak = max(longest_streak, curr_streak)
                    curr_streak = 1
        
        return max(longest_streak, curr_streak)

    # hashset: O(n)
    def longestConsecutive3(self, nums: list) -> int:
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                    
                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak

nums1 = [100,4,200,1,3,2] # 4
nums2 = [0,3,7,2,5,8,4,6,0,1] # 9
