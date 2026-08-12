class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        operations = 0

        for num in nums:
            #探索したい値
            target = k - num

            #探索値があれば削除回数(operations)を+1 countを減らす
            if count.get(target, 0) > 0:
                operations += 1
                count[target] -= 1
            
            else:
                count[num] = count.get(num, 0) + 1
        
        return operations
