class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_count = len(nums)

        flag = 0
        delete_index = []
        for i in range(nums_count):
            if nums[i]==0:
                flag += 1
                delete_index.append(i)
        
        for index in sorted(delete_index, reverse=True):
            del nums[index]
        
        nums.extend([0]*flag)
                
                
            
        