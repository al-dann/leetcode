"""18. 4Sum
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [], target = 0
Output: []

"""

class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return self.k_sum(nums, 4, target)

    def k_sum(self, nums: list[int], rank: int, target: int) -> list[list[int]]:
        if len(nums) < rank or nums[0] * rank > target or target > nums[-1] * rank:
            return []

        if rank == 2:
            return self.two_sum(nums, target)

        res = []
        for i in range(len(nums)):
            if not res or nums[i] != nums[i - 1]:
                for new_set in self.k_sum(nums[i + 1:], rank - 1, target - nums[i]):
                    res.append([nums[i]] + new_set)

        return res

    def two_sum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        sss = set()
        for val in nums:
            if not res or res[-1][1] != val:
                if val in sss:
                    res.append([target - val, val])
            sss.add(target - val)
        return res

# Runtime: 80 ms, faster than 97.85% of Python3 online submissions for 4Sum.
# Memory Usage: 14.2 MB, less than 82.22% of Python3 online submissions for 4Sum.


if __name__ == '__main__':
    my_solution = Solution()
    n_list = [1,0,-1,0,-2,2]
    tgt = 0
    print("input: {}".format(n_list))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.four_sum(n_list, tgt)))
