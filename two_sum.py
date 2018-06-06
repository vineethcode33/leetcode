"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from collections import defaultdict
        my_hash_map = defaultdict(list)
        for each in nums:
            my_hash_map[each]= [i for i, x in enumerate(nums) if x == each]

        for each_val in my_hash_map:
            look_for = target - each_val
            if look_for in my_hash_map.keys():
                 return [my_hash_map[each_val][-1:][0], my_hash_map[look_for][0]]