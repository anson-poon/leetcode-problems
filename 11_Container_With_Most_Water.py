
# https://leetcode.com/problems/container-with-most-water/

def maxArea(height) -> int:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    if not height:
        return 0
    
    left, right = 0, len(height) - 1    # left right pointers at first and last index
    max_area = 0

    while left < right:
        # calculate area, if area bigger than max_area, update max_area, increment/decrement pointer at lower height
        if height[left] < height[right]:
            cur_area = height[left] * (right - left)
            left += 1
        else:
            cur_area = height[right] * (right - left)
            right -= 1
        
        max_area = max(max_area, cur_area)
    
    return max_area

