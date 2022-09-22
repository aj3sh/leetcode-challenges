"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def merge_sorted_arr(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        new_arr = []
        new_arr_append = new_arr.append
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                new_arr_append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                new_arr_append(arr2[j])
                j += 1
            elif arr1[i] == arr2[j]:
                new_arr_append(arr1[i])
                new_arr_append(arr2[j])
                i += 1
                j += 1

        # adding remaining items
        while i < len(arr1):
            new_arr_append(arr1[i])
            i += 1
        while j < len(arr2):
            new_arr_append(arr2[j])
            j += 1

        return new_arr

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = self.merge_sorted_arr(nums1, nums2)
        
        # odd length
        if len(sorted_arr) % 2 == 1:
            return sorted_arr[ len(sorted_arr) // 2]
        
        # even length
        return (sorted_arr[len(sorted_arr) // 2 -1] + sorted_arr[ len(sorted_arr) // 2 ]) / 2

# Time Complexity: O(n)
# Space Complexity: O(1)