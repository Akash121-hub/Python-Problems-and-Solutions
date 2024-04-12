"""217. Contains Duplicate
Solved
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false"""

class ContainsDuplicate:
    def duplicate_exists(self,nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False