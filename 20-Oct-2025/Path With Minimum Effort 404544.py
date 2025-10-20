# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        jumps = [[float('inf')] * COLS for _ in range(ROWS)]
        jumps[0][0] = 0
        queue = [(0, (0, 0))]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        while queue:
            jump, cell = heapq.heappop(queue)
            if cell in visited:
                continue
            
            visited.add(cell)
            if cell == (ROWS - 1, COLS - 1):
                return jump
            
            for dr, dc in directions:
                nr, nc = cell[0] + dr, cell[1] + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    next_jump = max(
                        jump,
                        abs(heights[nr][nc] - heights[cell[0]][cell[1]])
                    )
                    if next_jump < jumps[nr][nc]:
                        jumps[nr][nc] = next_jump
                        heapq.heappush(queue, (next_jump, (nr, nc)))