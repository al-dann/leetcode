"""40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate numbers
sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[[1,2,2],[5]]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:

        def dfs(idx: int, tgt: int, arr: list[int]):
            # print("tgt: {};\tidx: {};\tarr: {}".format(tgt, idx, arr))
            if tgt == 0:
                result.append(arr)
                # print(result)
            elif tgt > 0:
                for j in range(idx, c_len):
                    if j > idx and candidates[j] == candidates[j-1]:
                        continue
                    value = candidates[j]
                    if tgt >= value:
                        dfs(j + 1, tgt - value, arr + [value])
            return

        result = []
        candidates.sort()
        c_len = len(candidates)
        dfs(0, target, [])
        return result

# Runtime: 64 ms, faster than 67.26% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14.4 MB, less than 20.13% of Python3 online submissions for Combination Sum II.

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [10, 1, 2, 7, 6, 1, 5]
    # in_lst = [2,5,2,1,2]

    in_lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    tgt = 27
    in_lst = [1, 1, 1, 1, 1]
    tgt = 3
    # tgt = 8
    print("input: {}".format(in_lst))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.combination_sum(in_lst, tgt)))
