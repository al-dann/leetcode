"""1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        inv_dic = {}
        for idx, val in enumerate(nums):
            inv_tgt = target - val
            if val in inv_dic:
                return {idx, inv_dic[val]}
            inv_dic[inv_tgt] = idx

        return []


# Runtime: 36 ms, faster than 99.18% of Python3 online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 91.48% of Python3 online submissions for Two Sum.

if __name__ == '__main__':
    my_solution = Solution()
    tst_1 = [-12, 0, 1, 2, 7, 11, 15]
    tgt_1 = 8
    print("Test list: {}".format(tst_1))
    print("Target: {}".format(tgt_1))
    print("Result: {}".format(my_solution.twoSum(tst_1, tgt_1)))
