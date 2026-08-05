class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        left = 0
        right = len(chars) -1

        while left < right:
            #左から母音を探す
            while left < right and chars[left] not in vowels:
                left += 1
            
            #右から母音を探す
            while left < right and chars[right] not in vowels:
                right -= 1
            
            #左右の母音を入れ替える
            chars[left], chars[right] = chars[right], chars[left]

            left += 1
            right -= 1

        return "".join(chars)

        