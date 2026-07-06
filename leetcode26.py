'''

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_num = set()
        curr = 0
        index = 0

        while index<len(nums):
            if nums[index] not in unique_num:
                nums[curr] = nums[index]
                unique_num.add(nums[index])
                curr += 1
            index+=1

        return len(unique_num)
