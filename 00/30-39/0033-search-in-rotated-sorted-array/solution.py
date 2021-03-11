"""33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot
index k (0 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index
 of target if it is in nums, or -1 if it is not in nums.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1


Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] == target:
            return 0
        l_idx = 0
        r_idx = len(nums) - 1
        while l_idx < r_idx:
            i = (r_idx + l_idx) // 2
            # print(i)
            if nums[i] == target:
                return i
            elif nums[l_idx] < nums[i]:
                if nums[l_idx] <= target < nums[i]:
                    r_idx = i
                else:
                    l_idx = i
            elif nums[l_idx] > nums[i]:
                if nums[i] < target <= nums[r_idx]:
                    l_idx = i
                else:
                    r_idx = i
            elif nums[r_idx] == target:
                return r_idx
            else:
                return -1
        return -1

        return


# Runtime: 44 ms, faster than 50.08% of Python3 online submissions
# Memory Usage: 14.7 MB, less than 24.17% of Python3 online submissions

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [1]
    in_lst = [4, 6, 7, 8, 0, 1, 2]
    tgt = 4
    print("input: {}".format(in_lst))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.search(in_lst, tgt)))
