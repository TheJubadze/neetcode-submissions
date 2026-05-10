class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        a = ord('a')
        for ch in s:
            letters[ord(ch) - a] += 1
        for ch in t:
            letters[ord(ch) - a] -= 1
        return all(l == 0 for l in letters)