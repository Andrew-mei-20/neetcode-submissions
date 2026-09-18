class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        right = 0
        left = 0
        longest = 0
        while right < len(s):
            if s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            else:
                mySet.add(s[right])
                right += 1
                longest = max(longest, right - left)
        return longest
