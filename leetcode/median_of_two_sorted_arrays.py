from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        while True:
            l2 = len(nums2)
            l1 = len(nums1)

            if 0 in (l1, l2) or (l1 == 1 and l2 == 1):
                break

            if nums1[-1] >= nums2[-1]:
                del nums1[-1]
            else:
                del nums2[-1]

            l2 = len(nums2)
            l1 = len(nums1)

            if l1 == 0:
                del nums2[0]
                continue
            if l2 == 0:
                del nums1[0]
                continue

            if nums1[0] <= nums2[0]:
                del nums1[0]
            else:
                del nums2[0]

        median = sorted(nums1 + nums2)
        return self.findMedian(median)

    def findMedian(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2


print(Solution().findMedianSortedArrays([4], [1, 2, 3]))
