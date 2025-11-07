# Merge two sorted lists


#  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         i = m - 1
#         j = n - 1
#         k = m + n - 1
#         while(i >= 0 and j >= 0):
#             if(nums1[i] > nums2[j]):
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else :
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1
#         while(j >= 0):
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1
        


# Remove Duplicates


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         k = 1
#         length = len(nums)
#         for i in range(1, length):
#             prev = nums[i - 1]
#             if(prev != nums[i]):
#                 nums[k] = nums[i]
#                 k += 1  
#         return k



# Move Zeros

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = 0
#         for i in range(1, len(nums)):
#             if(nums[k] == 0):
#                 nums[k], nums[i] = nums[i], nums[k]
#             if(nums[k] != 0): k += 1
        


        