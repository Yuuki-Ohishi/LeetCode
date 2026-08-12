class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Two Pointerを使用
        left_index = 0
        right_index = len(height) - 1

        x_water = right_index - left_index
        y_water = min(height[left_index], height[right_index])

        current_water_container = x_water * y_water

        for i in range(1, len(height)):
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1
            
            #左右が同じになったら終了
            if left_index == right_index:
                break

            #コンテナに溜まる水の量を計算
            x_water = right_index - left_index
            y_water = min(height[left_index], height[right_index])
            water_container = x_water * y_water

            if water_container < current_water_container:
                pass
            else:
                current_water_container = water_container

        return current_water_container







        