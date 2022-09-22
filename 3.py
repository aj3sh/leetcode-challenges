"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_char = ''
        current_char = ''
        
        main_cursor = 0
        moving_cursor = 0
        while main_cursor < len(s) and moving_cursor < len(s):
            if s[moving_cursor] in current_char:
                if len(longest_char) <= len(current_char):
                    longest_char = current_char
                current_char = ''
                main_cursor += 1
                moving_cursor = main_cursor
            
            current_char += s[moving_cursor]
            moving_cursor += 1
        
        if len(longest_char) <= len(current_char):
            longest_char = current_char
            
        return len(longest_char)

# Time Complexity: O(n)
# Space Complexity: O(1)