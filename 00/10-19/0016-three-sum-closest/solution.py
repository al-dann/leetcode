"""16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""

class Solution:
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        delta = abs(result - target)
        vis_set = set()
        nums_len = len(nums)
        for i in range(nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                tmp_tgt = nums[i] + nums[j] - target
                if tmp_tgt not in vis_set:
                    for k in range(j + 1, nums_len):
                        test_delta = abs(tmp_tgt + nums[k])
                        if test_delta < delta:
                            delta = test_delta
                            result = tmp_tgt + target + nums[k]
                        if delta == 0:
                            return result
                else:
                    vis_set.add(tmp_tgt)
        return result

# Runtime: 656 ms, faster than 6.37% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.4 MB, less than 45.82% of Python3 online submissions for 3Sum Closest.


if __name__ == '__main__':
    my_solution = Solution()
    n_list = [-1,2,1,-4]
    tgt = 1
    print("input: {}".format(n_list))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.three_sum_closest(n_list, tgt)))
