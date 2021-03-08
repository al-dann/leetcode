"""11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2


Example 4:
Input: height = [2,3,4,5,18,17,6]
Output: 17

"""

class Solution:
    def max_area(self, height: list[int]) -> int:
        max_vol = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                vol = (j - i) * height[i]
                i += 1
            else:
                vol = (j - i) * height[j]
                j -= 1
            max_vol = max(max_vol, vol)
        return max_vol

# Runtime: 676 ms, faster than 5.25% of Python3 online submissions
# Memory Usage: 28 MB, less than 20.63% of Python3 online submissions


if __name__ == '__main__':
    my_solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    # height = [1,8,6,2,5,4,16,3,10]
    # height = [1, 1]
    # height = [4, 3, 2, 1, 4]
    # height = [1, 2, 1]
    # height = [2, 3, 4, 5, 18, 17, 6]
    print("height: {}".format(height))
    print("result: {}".format(my_solution.max_area(height)))
