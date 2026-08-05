class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):
            # 現在の位置が空いているか
            current_empty = flowerbed[i] == 0

            # 先頭、または左隣が空いているか
            left_empty = i == 0 or flowerbed[i - 1] == 0

            # 末尾、または右隣が空いているか
            right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            # 3条件をすべて満たす場合
            if current_empty and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
        return n <= 0
