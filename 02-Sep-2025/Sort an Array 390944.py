# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution(object):
    def sortArray(self, nums):
        def mergeSort(array):            
            size = len(array)
            if size <= 1:
                return array

            mid = size // 2
            left = mergeSort(array[:mid])
            right = mergeSort(array[mid:])
            
            answer = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    answer.append(left[i])
                    i += 1
                else:
                    answer.append(right[j])
                    j += 1
            
            answer.extend(left[i:])
            answer.extend(right[j:])
            
            return answer

        return mergeSort(nums)
