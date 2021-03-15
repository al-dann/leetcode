"""39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target.You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
times. 7 is a candidate, and 7 = 7. These are the only two combinations.

Example 2:
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1, 1]]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:

        def dfs(tst_lst: list[int], tgt: int, arr: list[int]):
            # print("tgt: {};\ttst_lst: {};\tarr: {}".format(tgt, tst_lst, arr))
            if tgt == 0:
                res_lst.append(arr)
                # print(res_lst)
            elif tgt > 0:
                for item, value in enumerate(tst_lst):
                    if tgt >= value:
                        dfs(tst_lst[item:], tgt - value, arr + [value])
            return

        res_lst = []
        dfs(candidates, target, [])

        return res_lst

# Runtime: 60 ms, faster than 80.96% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.4 MB, less than 54.41% of Python3 online submissions for Combination Sum.

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [2, 3, 6, 7]
    # in_lst = [1,3,5,6]
    tgt = 7
    print("input: {}".format(in_lst))
    print("target: {}".format(tgt))
    print("result: {}".format(my_solution.combination_sum(in_lst, tgt)))


"""
Test printing:

/usr/local/bin/python3.9 /Users/alex/PycharmProjects/leetcode_scratch/main.py
input: [2, 3, 6, 7]
target: 7
tgt: 7; tst_lst: [2, 3, 6, 7];  arr: []
tgt: 5; tst_lst: [2, 3, 6, 7];  arr: [2]
tgt: 3; tst_lst: [2, 3, 6, 7];  arr: [2, 2]
tgt: 1; tst_lst: [2, 3, 6, 7];  arr: [2, 2, 2]
tgt: 0; tst_lst: [3, 6, 7]; arr: [2, 2, 3]
[[2, 2, 3]]
tgt: 2; tst_lst: [3, 6, 7]; arr: [2, 3]
tgt: 4; tst_lst: [3, 6, 7]; arr: [3]
tgt: 1; tst_lst: [3, 6, 7]; arr: [3, 3]
tgt: 1; tst_lst: [6, 7];    arr: [6]
tgt: 0; tst_lst: [7];   arr: [7]
[[2, 2, 3], [7]]
result: [[2, 2, 3], [7]]
"""
