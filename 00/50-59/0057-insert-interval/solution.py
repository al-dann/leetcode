"""57. Insert Interval
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to
their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 10^5
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 10^5
"""


class Solution:
    def insert(self, intervals: list[list[int]], new_int: list[int]) -> list[list[int]]:
        if not intervals:
            return [new_int]
        if intervals[-1][1] < new_int[0]:
            intervals.extend([new_int])
            return intervals
        if new_int[1] < intervals[0][0]:
            result = [new_int]
            result.extend(intervals)
            return result

        # find upper bound index
        u_pos = len(intervals) - 1
        for idx, val in enumerate(intervals):
            if new_int[1] < val[0]:
                u_pos = idx - 1
                break
        # find lower bound index
        l_pos = 0
        for idx in range(len(intervals) - 1, -1, -1):
            if intervals[idx][1] < new_int[0]:
                l_pos = idx + 1
                break
        # compose the result
        result = intervals[0:l_pos]
        middle = [min(intervals[l_pos][0], new_int[0]), max(intervals[u_pos][1], new_int[1])]
        result.append(middle)
        result.extend(intervals[u_pos + 1:])
        return result

# Runtime: 76 ms, faster than 88.21% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.5 MB, less than 72.49% of Python3 online submissions for Insert Interval.

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [[1, 3], [6, 9], [11, 14]]
    in_lst = []
    in_val = [0, 0]

    print("input: {}".format(in_lst))
    print("target: {}".format(in_val))
    print("result: {}".format(my_solution.insert(in_lst, in_val)))
