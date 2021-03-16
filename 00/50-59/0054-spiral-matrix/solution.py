"""54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        height = len(matrix)
        length = len(matrix[0])
        result = []
        lo_height_idx = 0
        hi_height_idx = height - 1
        lo_length_idx = 0
        hi_length_idx = length - 1
        while len(result) < height * length:
            # move right
            if lo_height_idx <= hi_height_idx:
                result.extend(matrix[lo_height_idx][lo_length_idx:hi_length_idx + int(lo_height_idx == hi_height_idx)])
            # move down
            if lo_height_idx < hi_height_idx:
                for i in range(lo_height_idx, hi_height_idx + int(lo_length_idx == hi_length_idx)):
                    result.append(matrix[i][hi_length_idx])
                # move left
                result.extend(matrix[hi_height_idx][hi_length_idx:lo_length_idx:-1])
                # and move up
                if lo_length_idx < hi_length_idx:
                    for j in range(hi_height_idx, lo_height_idx, -1):
                        result.append(matrix[j][lo_length_idx])
            # shift indexes
            lo_height_idx += 1
            hi_height_idx -= 1
            lo_length_idx += 1
            hi_length_idx -= 1
        return result

# Runtime: 32 ms, faster than 63.03% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.4 MB, less than 32.88% of Python3 online submissions for Spiral Matrix.

if __name__ == '__main__':
    my_solution = Solution()
    # in_lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    in_lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # in_lst = [[1,2,3],[4,5,6],[7,8,9]]
    # in_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # in_lst = [[1, 2, 3]]
    # in_lst = [[1]]
    # in_lst = [[1], [2], [3]]
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    print("result: {}".format(my_solution.spiral_order(in_lst)))
