class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = []
        nums.sort()

        n = len(nums)

        for i in range(n-2):

            if i>0 and nums[i]==nums[i-1]:
                continue

            current_sum = -1*nums[i]

            left = i+1
            right = n-1

            while left<right:
                if nums[left]+nums[right]+nums[i]>0:
                    right -= 1
                    continue
                elif nums[left]+nums[right]+nums[i]<0:
                    left += 1
                    continue
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result