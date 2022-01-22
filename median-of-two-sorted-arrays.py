from typing import List


class Solution:
    def find_kth(self, nums1, nums2, start1, end1, start2, end2, k) -> float:
        while start1 <= end1 and start2 <= end2:
            mid1, mid2 = (start1 + end1) // 2, (start2 + end2) // 2

            if mid1 + mid2 < k:
                if nums1[mid1] > nums2[mid2]:
                    start2 = mid2 + 1
                else:
                    start1 = mid1 + 1
            else:
                if nums1[mid1] > nums2[mid2]:
                    end1 = mid1 - 1
                else:
                    end2 = mid2 - 1

        return nums2[k - start1] if start1 > end1 else nums1[k - start2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        k = (n + m) // 2

        if (n + m) % 2:
            return self.find_kth(nums1, nums2, 0, n - 1, 0, m - 1, k)

        v1 = self.find_kth(nums1, nums2, 0, n - 1, 0, m - 1, k)
        v2 = self.find_kth(nums1, nums2, 0, n - 1, 0, m - 1, k - 1)
        return (v1 + v2) / 2


if __name__ == '__main__':
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1, 2, 3], []) == 2
    assert solution.findMedianSortedArrays([], [1, 2, 3]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([3, 4], [1, 2]) == 2.5
    assert solution.findMedianSortedArrays([1, 2, 2], [1, 2, 3]) == 2
