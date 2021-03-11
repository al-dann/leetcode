"""31. Next Permutation
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:gcloud
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

class Solution:
    def next_permutation(self, nums: list[int]) -> None:
        n_len = len(nums)
        if n_len == 1:
            return
        for i in range(n_len - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(n_len - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        break
                for k in range(i + 1, i + 1 + (n_len - i) // 2):
                    nums[k], nums[n_len - k + i] = nums[n_len - k + i], nums[k]
                return
        # we should reverse the whole array
        for p in range(n_len // 2):
            nums[p], nums[n_len - 1 - p] = nums[n_len - 1 - p], nums[p]
        return


# Runtime: 44 ms, faster than 63.45% of Python3 online submissions for Next Permutation.
# Memory Usage: 14.2 MB, less than 57.40% of Python3 online submissions for Next Permutation.

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [3, 2, 2, 3]
    # in_lst = [0, 1, 2, 2, 3, 0, 4, 2]
    # in_lst = [3, 3]
    in_lst = [1, 2, 3]
    # in_lst = [4, 7, 6, 5, 4, 3, 2, 2, 1]
    # in_lst = [1, 5, 2]
    print("input: {}".format(in_lst))
    my_solution.next_permutation(in_lst)
    print("result: {}".format(in_lst))
