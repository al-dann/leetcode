"""55. Jump Game
https://leetcode.com/problems/spiral-matrix/

Given an array of non-negative integers nums, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5
"""


class Solution:
    def can_jump(self, nums: list[int]) -> bool:
        tgt_idx = len(nums) - 1
        for curr_idx in range(tgt_idx - 1, -1, -1):
            if nums[curr_idx] >= tgt_idx - curr_idx:
                tgt_idx = curr_idx
        return tgt_idx == 0

# Runtime: 80 ms, faster than 94.02% of Python3 online submissions for Jump Game.
# Memory Usage: 15.9 MB, less than 99.91% of Python3 online submissions for Jump Game.

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [2,3,1,1,4]
    # in_lst = [3,2,1,0,4]
    # in_lst = [1]
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    print("result: {}".format(my_solution.can_jump(in_lst)))
