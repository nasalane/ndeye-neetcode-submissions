class Solution:
    def longestPalindrome(self, s: str) -> str:

        #         Idea
        # Every palindrome has a center:
        # Odd length: center is one character (racecar → e)
        # Even length: center is between two characters (abba → between the two bs)
        # For each index, expand outward while the characters match.
        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd-length palindrome
            l2, r2 = expand(i, i + 1)   # even-length palindrome

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]