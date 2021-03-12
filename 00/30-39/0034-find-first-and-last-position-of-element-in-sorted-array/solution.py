"""34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        l_idx: int = 0
        r_idx: int = len(nums) - 1
        while l_idx <= r_idx:
            mid: int = (l_idx + r_idx) // 2
            if nums[mid] < target:
                l_idx = mid + 1
            elif nums[mid] > target:
                r_idx = mid - 1
            else:
                min_idx = self.search_min_idx(nums, mid, l_idx)
                max_idx = self.search_max_idx(nums, mid, r_idx)
                return [min_idx, max_idx]
        return [-1, -1]

    def search_min_idx(self, nums: list[int], tgt_idx: int, min_idx: int) -> int:
        target: int = nums[tgt_idx]
        l_idx: int = min_idx
        r_idx: int = tgt_idx
        while l_idx <= r_idx:
            mid: int = (l_idx + r_idx) // 2
            if nums[mid] < target:
                l_idx = mid + 1
            else:
                r_idx = mid - 1
        return l_idx

    def search_max_idx(self, nums: list[int], tgt_idx: int, max_idx: int) -> int:
        target: int = nums[tgt_idx]
        l_idx: int = tgt_idx
        r_idx: int = max_idx
        while l_idx <= r_idx:
            mid: int = (l_idx + r_idx) // 2
            if nums[mid] > target:
                r_idx = mid - 1
            else:
                l_idx = mid + 1
        return r_idx

# Runtime: 84 ms, faster than 74.72% of Python3 online submissions
# Memory Usage: 15.3 MB, less than 82.68% of Python3 online submissions

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [8]
    in_lst = [8, 8, 12]
    tgt = 8
    print("input: {}".format(in_lst))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.search_range(in_lst, tgt)))
