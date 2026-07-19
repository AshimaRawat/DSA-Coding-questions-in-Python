'''
Longest Substring Without Repeating Characters
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0
        start = 0
        for right , ch in enumerate(s):
            if ch in last_seen and last_seen[ch]>=left:
                left = last_seen[ch]+1
            last_seen[ch] = right
            current_len = right-left+1
            if current_len>longest:
                longest = current_len
                start = left
        return s[start: start+longest]
        
