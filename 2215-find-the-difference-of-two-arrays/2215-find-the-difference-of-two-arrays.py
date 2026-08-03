class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums2 = list(dict.fromkeys(nums2))
        nums1 = list(dict.fromkeys(nums1))

        nums1_new = []
        for i in nums1:
            print(i)
            if i in nums2:
                nums2 = [nums2 for nums2 in nums2 if nums2 != i]

            else:
                nums1_new.append(i)
        
        result = [nums1_new, nums2]
        return result