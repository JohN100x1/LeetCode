class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checked = {}
        max_counter = 0
        i = 0
        for j, c in enumerate(s):
            if c in checked.keys():
                i = max(checked[c], i)
            max_counter = max(max_counter, j - i + 1)
            checked[c] = j + 1
        return max_counter
