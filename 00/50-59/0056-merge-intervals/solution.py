"""56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4
"""


class Solution:
    # def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    #     sorted_lst = sorted(intervals, key=lambda interval: interval[0])
    #     result = [sorted_lst[0]]
    #     for i in range(1, len(sorted_lst)):
    #         if result[-1][1] >= sorted_lst[i][1]:
    #             continue
    #         elif result[-1][1] < sorted_lst[i][0]:
    #             result.append(sorted_lst[i])
    #         else:
    #             result[-1][1] = sorted_lst[i][1]
    #     return result

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_lst = sorted(intervals, key=lambda interval: interval[0])
        result = [sorted_lst[0]]
        for i in range(1, len(sorted_lst)):
            if result[-1][1] < sorted_lst[i][0]:
                result.append(sorted_lst[i])
            elif result[-1][1] < sorted_lst[i][1]:
                result[-1][1] = sorted_lst[i][1]
        return result


# Runtime: 76 ms, faster than 97.70% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16 MB, less than 85.38% of Python3 online submissions for Merge Intervals.

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [[1,3], [2,6], [8,10], [15,18]]
    # in_lst = [[1,4],[4,5], [1,6]]
    # in_lst = [[1,4],[5,6]]
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    print("result: {}".format(my_solution.merge(in_lst)))
