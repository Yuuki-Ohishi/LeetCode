class Solution:
    def removeStars(self, s: str) -> str:
        str_list = []

        #*の時はリスト後ろから取り出し、それ以外はlist格納
        for char in s:
            if char == "*":
                str_list.pop()
            
            else:
                str_list.append(char)
        
        return "".join(str_list)
