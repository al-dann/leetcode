"""4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

"""

# class Solution:
#     def find_median_sorted_arrays(self, nums1: list, nums2: list) -> float:
#         joined_list = nums1
#         joined_list.extend(nums2)
#         joined_list = sorted(joined_list)
#         total_len = len(joined_list)
#         is_even = 1 - total_len % 2
#         mid_idx = total_len // 2
#         return (joined_list[mid_idx] + joined_list[mid_idx - is_even]) / 2

# Runtime: 92 ms, faster than 71.36% of Python3 online submissions
# Memory Usage: 14.7 MB, less than 7.31% of Python3 online submissions


class Solution:
    def find_median_sorted_arrays(self, nums1: list, nums2: list) -> float:
        idx1 = 0
        idx2 = 0
        len2 = len(nums2)
        len1 = len(nums1)
        tot_len = len1 + len2
        is_even = 1 - tot_len % 2
        med_idx = tot_len // 2 - is_even
        for idx, itm in enumerate(nums1):
            while (idx2 < len2) and (idx + idx2 < med_idx):
                if nums2[idx2] <= itm:
                    idx2 += 1
                else:
                    break
            if idx + idx2 == med_idx:
                idx1 = idx
                break
        if idx1 + idx2 != med_idx:
            idx1 = len1
            idx2 = med_idx - idx1
        m_list = nums1[idx1: idx1 + 2]
        m_list.extend(nums2[idx2: idx2 + 2])
        m_list = sorted(m_list)
        print(m_list)
        if len(m_list) == 1 or not is_even:
            return m_list[0]
        return (m_list[0] + m_list[1]) / 2

# Runtime: 88 ms, faster than 85.39% of Python3 online submissions
# Memory Usage: 14.7 MB, less than 27.70% of Python3 online submissions


if __name__ == '__main__':
    my_solution = Solution()
    nums1 = [0, 0]
    nums2 = [0, 0]
    print("Array 1: {}".format(nums1))
    print("Array 2: {}".format(nums2))
    print("Result: {}".format(my_solution.find_median_sorted_arrays(nums1, nums2)))
