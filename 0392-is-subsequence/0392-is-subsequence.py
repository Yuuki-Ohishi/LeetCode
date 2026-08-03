class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        match_str = 0
        for char in t:
            if s[match_str] == char:
                match_str += 1
                if match_str==len(s):
                    return True
        return False

