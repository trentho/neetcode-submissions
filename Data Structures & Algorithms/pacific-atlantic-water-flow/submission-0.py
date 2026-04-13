class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r,c, visited, prevHeight):
            # check bounds and check for our special case where we want to go up in heights not down
            if r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight or (r,c) in visited:
                return

            visited.add((r,c))

            # explore the 4 directions (up, down, left, right)
            dfs(r + 1,c,visited, heights[r][c])
            dfs(r - 1,c,visited, heights[r][c])
            dfs(r,c + 1,visited, heights[r][c])
            dfs(r,c - 1,visited, heights[r][c])

        # dfs on the columns that border pacific and atlantic
        for c in range(COLS):
            # pacific
            dfs(0, c, pac, heights[0][c])

            # last row which is atlantic
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        # dfs on the rows that border pacific and atlantic
        for r in range(ROWS):
            # pacific
            dfs(r, 0, pac, heights[r][0])

            # last row which is atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])            


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res