class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitudes = 0
        max_altitudes = 0
        for i in gain:
            current_altitudes += i
            
            max_altitudes = max(max_altitudes, current_altitudes)
            
        return max_altitudes