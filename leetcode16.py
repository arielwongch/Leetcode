"""

"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i+1
            right = n-1
            while left<right:
                diff = abs(closest_sum -target)
                curr_sum = nums[i]+nums[left]+nums[right]
                if abs(curr_sum-target)<diff:
                    closest_sum = curr_sum
                if curr_sum -target> 0:
                    right-=1
                else:
                    left+=1
        return closest_sum