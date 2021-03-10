"""15. Three Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

"""

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        res_set = set()
        tst_lst = []
        for i in range(len(nums) - 2):
            if nums[i] not in tst_lst:
                res_set |= self.two_sum(nums, i + 1, nums[i])
                tst_lst.append(nums[i])

        return list(res_set)

    def two_sum(self, nums: list, start_pos: int, base: int) -> set:
        ret_set = set()
        inv_set = set()
        for idx in range(start_pos, len(nums)):
            val = nums[idx]
            if val in inv_set:
                triple = tuple(sorted([base, val, -1 * (val + base)]))
                ret_set.add(triple)
            else:
                inv_set.add(-1 * (val + base))
        return ret_set

# Runtime: 1084 ms, faster than 48.18% of Python3 online submissions for 3Sum.
# Memory Usage: 17.4 MB, less than 75.06% of Python3 online submissions for 3Sum.

if __name__ == '__main__':
    my_solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print("input: {}".format(nums))
    print("result: {}".format(my_solution.three_sum(nums)))
