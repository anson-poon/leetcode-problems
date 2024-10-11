def numIslands(grid) -> int:
    # use dfs on each tile, mark tiles as visited. once no more tiles to visit, increment island count
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    island_count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == "0":
            return

        visited.add((r, c))

        # Explore neighboring tiles
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

        return True

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                if dfs(i, j):
                    island_count += 1

    return island_count

