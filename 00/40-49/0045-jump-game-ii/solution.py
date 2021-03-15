"""45. Jump Game II
https://leetcode.com/problems/combination-sum-ii/

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^5
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        min_idx = len(nums) - 1
        step_nm = 0
        while min_idx > 0:
            tgt_idx = min_idx
            for curr_idx in range(tgt_idx - 1, -1, -1):
                if nums[curr_idx] >= tgt_idx - curr_idx:
                    min_idx = curr_idx
            step_nm += 1

        return step_nm

# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Jump Game II.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Jump Game II.


if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [2,3,1,1,4]
    in_lst = [2,3,0,1,4]
    in_lst = [1, 0, 1]
    # tgt = 8
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    print("result: {}".format(my_solution.jump(in_lst)))
