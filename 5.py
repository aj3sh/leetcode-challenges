"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    
    def check_window(self, s, start, end,largest_palindrome=''):
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            elif len(largest_palindrome) < end-start+1:
                    largest_palindrome = s[start:end+1]

            # start and end increment
            start -= 1
            end += 1
        
        return largest_palindrome
    
    def longestPalindrome(self, s: str) -> str:
        largest_palindrome = s[0] # making default with first string
        
        for i in range(len(s)):
            largest_palindrome = self.check_window(s, i, i+1, largest_palindrome=largest_palindrome)
            largest_palindrome = self.check_window(s, i-1, i+1, largest_palindrome=largest_palindrome)

        return largest_palindrome
