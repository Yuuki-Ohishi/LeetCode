class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_box = list(word1)
        word2_box = list(word2)
        box = []

        if len(word1_box) > len(word2_box):
            char = len(word1_box)

        elif len(word1_box) < len(word2_box):
            char = len(word2_box)

        elif len(word2_box) == len(word1_box):
            char = len(word1_box)            
            
        for i in range(char):
            if i <= len(word1_box)-1:
                box.append(word1_box[i])
            else:
                pass
            
            if i <= len(word2_box)-1:
                box.append(word2_box[i])
            else:
                pass
        
        word = "".join(box)

        return word
