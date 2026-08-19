class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                #12などの複数桁にも対応
                current_num = current_num * 10 + int(char)
            
            elif char == "[":
                #[より前の文字列と繰り返し回数を保存
                stack.append((current_string, current_num))

                #[]内の文字列を作るために初期化
                current_string = ""
                current_num = 0
            
            elif char == "]":
                #[より前の状態を取り出す
                previous_string, repeat_num = stack.pop()

                #[]内の文字列を指定回数繰り返す
                current_string = (
                    previous_string
                    + current_string *repeat_num
                )
            
            else:
                #通常のアルファベッド
                current_string += char
        
        return current_string