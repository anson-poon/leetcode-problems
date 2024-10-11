'''
This problem is not from leetcode, it is a modification of the "200. Number of Islands" problem.
The difference is that each island may contain treasure(s) represented by 'T',
and we need to return the number of islands that contain treasure(s)
'''


def numIslandsWithTreasure(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def dfs(r, c):
        # If out of bounds or already visited or it's water, stop recursion
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == '0':
            return False
        
        # Mark current cell as visited
        visited.add((r, c))
        
        # Check if the current cell has treasure
        has_treasure = (grid[r][c] == 'T')
        
        # Explore the neighboring cells
        has_treasure = dfs(r - 1, c) or has_treasure  # up
        has_treasure = dfs(r + 1, c) or has_treasure  # down
        has_treasure = dfs(r, c - 1) or has_treasure  # left
        has_treasure = dfs(r, c + 1) or has_treasure  # right
        
        # # Alternative: Explore the neighboring cells with a loop
        # for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #     has_treasure |= dfs(r + dr, c + dc)
        
        return has_treasure
    
    island_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['1', 'T'] and (r, c) not in visited:
                # Run DFS for each new island
                if dfs(r, c):
                    island_count += 1

    return island_count


# Example usage:
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "T", "0", "0", "0"],
  ["0", "0", "1", "0", "T"],
  ["0", "0", "0", "1", "1"]
]

print(numIslandsWithTreasure(grid))  # Output: 2 (two islands contain treasures)
