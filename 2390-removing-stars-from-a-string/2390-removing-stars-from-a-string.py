class Solution:
    def removeStars(self, s: str) -> str:
        stack_list = []

        #*の時はリスト後ろから取り出し、それ以外はlist格納
        for char in s:
            if char == "*":
                stack_list.pop()
            else:
                stack_list.append(char)
        
        return "".join(stack_list)
