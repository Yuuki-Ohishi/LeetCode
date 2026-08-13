class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        #最初のK文字に含まれる母音数
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_count = count

        #ウィンドウを右に動かす
        for i in range(k, len(s)):
            #新しく入ってくる文字
            if s[i] in vowels:
                count += 1
            
            #左から出ていく文字
            if s[i-k] in vowels:
                count -= 1

            max_count = max(max_count, count)
        
        return max_count