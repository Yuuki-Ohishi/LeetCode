class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            #新しく入った値が0ならカウント
            if nums[right] == 0:
                zero_count += 1
            
            #0がk個を超えたら左側を縮める
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
        
            #現在の範囲の長さ
            max_length = max(max_length, right - left + 1)
    
        return max_length

