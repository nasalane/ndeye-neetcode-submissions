class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # OPTIMIZATION: If the word is longer than the total cells, it's impossible.
        if len(word) > rows * cols:
            return False

        def backtrack(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            temp, board[r][c] = board[r][c], '#'
            
            # Using a loop for directions is often cleaner in interviews
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if backtrack(r + dr, c + dc, index + 1):
                    board[r][c] = temp # Always clean up before returning True
                    return True
            
            board[r][c] = temp # Backtrack
            return False

        # Must check every starting position
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]: # Optimization: Only start DFS on match
                    if backtrack(r, c, 0):
                        return True
        return False