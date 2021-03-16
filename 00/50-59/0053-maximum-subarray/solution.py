"""53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        max_sum = nums[0]
        arr_sum = nums[0]
        for idx in range(1, len(nums)):
            arr_sum = max(nums[idx], arr_sum + nums[idx])
            max_sum = max(max_sum, arr_sum)

        return max_sum

# Runtime: 68 ms, faster than 54.97% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 15 MB, less than 60.75% of Python3 online submissions for Maximum Subarray.

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [-2,1,-3,4,-1,2,1,-5,4]
    in_lst = [1]
    in_lst = [-2, -1]
    in_lst = [5,4,-1,7,8, -2]
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    print("result: {}".format(my_solution.max_sub_array(in_lst)))
