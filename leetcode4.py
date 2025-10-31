"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #we need to find kth smallest element

        #ensure num1 is smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m,n = len(nums1), len(nums2)

        low,high = 0,m

        while low<=high:
            i = (low+high)//2
            j = (m + n + 1) // 2 - i

            left1  = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]   if i < m else float('inf')
            left2  = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]   if j < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                # Found correct partition
                if (m + n) % 2 == 1:
                    return max(left1, left2)  # Odd length
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2 
            elif left1 > right2:
                high = i - 1   # Move left in nums1
            else:
                low = i + 1