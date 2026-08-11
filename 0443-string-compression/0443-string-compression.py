class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            #同じ文字が何個続いているか数える
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            #文字を書き込む
            chars[write] = char
            write += 1

            #2文字以上なら個数も書き込む
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write