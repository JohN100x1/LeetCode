class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        low = 0
        high = len(nums1) - 1
        for x in range(total):
            mid = (low + high) // 2
            idx = half - mid - 2
            if mid >= 0:
                left1 = nums1[mid]
            else:
                left1 = -pow(10, 6)
            if mid + 1 < len(nums1):
                right1 = nums1[mid + 1]
            else:
                right1 = pow(10, 6)
            if idx >= 0:
                left2 = nums2[idx]
            else:
                left2 = -pow(10, 6)
            if idx + 1 < len(nums2):
                right2 = nums2[idx + 1]
            else:
                right2 = pow(10, 6)
            if left2 > right1:
                low = mid + 1
            elif left1 > right2:
                high = mid - 1
            elif total % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return min(right1, right2)
