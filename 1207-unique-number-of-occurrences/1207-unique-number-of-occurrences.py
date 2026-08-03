class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(set(arr))==1:
            return True
        
        counts = Counter(arr)
        nums_count = Counter(list(counts.values()))
        
        unique_count = sum(count==1 for count in nums_count.values())

        if unique_count ==len(list(counts.values())):
            return True
        
        else:
            return False