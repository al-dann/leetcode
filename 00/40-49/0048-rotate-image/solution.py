"""48. Rotate Image
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:

        for lo_idx in range(len(matrix) // 2):
            hi_idx = len(matrix) - lo_idx
            # print("lo_idx: {}; hi_idx: {}".format(lo_idx, hi_idx))
            for i in range(0, hi_idx - lo_idx - 1):
                matrix[lo_idx + i][lo_idx], matrix[hi_idx - 1][lo_idx + i], \
                matrix[hi_idx - 1 - i][hi_idx - 1], matrix[lo_idx][hi_idx - 1 - i] = \
                matrix[hi_idx - 1][lo_idx + i], matrix[hi_idx - 1 - i][hi_idx - 1], \
                matrix[lo_idx][hi_idx - 1 - i], matrix[lo_idx + i][lo_idx]
                #
                # val_1 = matrix[lo_idx + i][lo_idx]          # left column, down direction
                # val_2 = matrix[hi_idx - 1][lo_idx + i]      # bottom row, right direction
                # val_3 = matrix[hi_idx - 1 - i][hi_idx - 1]  # right column, up direction
                # val_4 = matrix[lo_idx][hi_idx - 1 - i]      # top row, left direction
                # print(val_1, val_2, val_3, val_4)
                #
                # matrix[lo_idx + i][lo_idx] = val_2
                # matrix[hi_idx - 1][lo_idx + i] = val_3
                # matrix[hi_idx - 1 - i][hi_idx - 1] = val_4
                # matrix[lo_idx][hi_idx - 1 - i] = val_1
                # print(matrix)

# Runtime: 36 ms, faster than 63.97% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.4 MB, less than 33.00% of Python3 online submissions for Rotate Image.

if __name__ == '__main__':
    my_solution = Solution()
    in_lst = [[1,2,3],[4,5,6],[7,8,9]]
    in_lst = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    in_lst = [[1,2],[3,4]]
    in_lst = [[1]]
    print("input: {}".format(in_lst))
    # print("target: {}".format(tgt))
    my_solution.rotate(in_lst)
    print("result: {}".format(in_lst))
