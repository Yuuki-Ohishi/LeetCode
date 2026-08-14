class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right = 0
        left = 0
        zero_count = 0
        element_count = 0
        max_length = 0

        #要素全てを確認するまでループ
        while element_count < len(nums) :
            #要素が0の場合、カウント
            if nums[right] == 0:
                zero_count += 1

            #0のカウント数が1より大きい場合、左側を動かす
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            #0を含まない要素数を計算
            length = right - left + 1 - zero_count
            #0が1個以下で0を除いた最大の長さを保存
            max_length = max(max_length, length)

            right += 1
            element_count += 1

        #nums内に0が無かった時、1個削除
        if zero_count == 0:
            max_length -= 1

        return max_length
            
        

        