from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1

        while True:
            mid1 = (left + right) // 2
            mid2 = (n1 + n2) // 2 - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]

            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]

            if l1 > r2:
                right = mid1 - 1
            elif l2 > r1:
                left = mid1 + 1
            else:
                return min(r1, r2) if (n1 + n2) % 2 else (max(l1, l2) + min(r1, r2)) / 2


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1, 2, 3], []) == 2
    assert solution.findMedianSortedArrays([], [1, 2, 3]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([3, 4], [1, 2]) == 2.5
