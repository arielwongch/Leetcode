"""

"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        if n<4:
            return []

        result = []

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                left = j+1
                right = n-1

                while left<right:
                    if nums[left]+nums[right]+nums[i]+nums[j]==target:
                        result.append([nums[j],nums[i],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif nums[left]+nums[right]+nums[i]+nums[j]>target:
                        right-=1
                    else:
                        left+=1
        return result
        