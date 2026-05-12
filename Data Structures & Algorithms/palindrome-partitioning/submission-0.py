class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def isPalindrome(s: str) -> bool:
            # return s == s[::-1]
            left, right = 0, len(s) - 1
            
            # Continue until pointers meet or cross
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
                
            return True

        def backtrack(start: int):
            # Base case: reached the end of the string
            if start == len(s):
                res.append(list(path))
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)    # Choose
                    backtrack(end)            # Explore
                    path.pop()                # Backtrack (Undo)

        backtrack(0)
        return res