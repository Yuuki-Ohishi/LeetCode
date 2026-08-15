from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        #登場する文字の種類が異なる場合は変換できない
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        #出現回数の組み合わせが同じか確認する
        return sorted(count1.values()) == sorted(count2.values())