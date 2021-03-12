"""35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be
if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l_idx: int = 0
        r_idx: int = len(nums) - 1
        while l_idx <= r_idx:
            mid: int = (l_idx + r_idx) // 2
            if nums[mid] < target:
                l_idx = mid + 1
            elif nums[mid] > target:
                r_idx = mid - 1
            else:
                return mid
        return l_idx

# Runtime: 52 ms, faster than 48.91% of Python3 online submissions
# Memory Usage: 15.2 MB, less than 23.51% of Python3 online submissions

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [1]
    # in_lst = [1,3,5,6]
    tgt = 2
    print("input: {}".format(in_lst))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.search_insert(in_lst, tgt)))
