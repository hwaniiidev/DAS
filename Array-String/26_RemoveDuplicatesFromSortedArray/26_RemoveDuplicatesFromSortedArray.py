from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        my solution:
        The variable name min is misleading, and the logic is less standard than the two-pointer approach.
        While this code does pass the test cases due to the sorted nature of the input, it is unnecessarily complicated.
        """
        # k = 0
        # min = -101
        # for num in nums:
        #     if (min < num):
        #         min = num
        #         nums[k] = num
        #         k += 1
        # print(nums)
        # return k
        # It's not efficient because of the time complexity of sort(). This code's complexity is Big O of n squared (or Big O of n to the power of two)

        """
        better solution:
        The code employs the Two Pointers technique to remove duplicates from a sorted array in-place, 
        utilizing a write pointer (k) and a read pointer (i). The read pointer iterates through the array, 
        while the write pointer marks the position for the next unique element, starting at index 1. 
        If the element at the read pointer (nums[i]) is different from the previous element (nums[i-1]), 
        it signifies a new unique value. This unique value is then copied to the write position (nums[k]),
        and the write pointer k is incremented. 
        The process ensures that the first k elements of the original array contain the sorted, unique result, 
        and the function returns k, the count of unique numbers.
        """
        # Handle the edge case of an empty array
        if not nums:
            return 0

        # k is the index where the next unique element will be placed.
        # It also serves as the count of unique elements (k).
        k = 1

        # i iterates through the array from the second element (index 1).
        for i in range(1, len(nums)):
            # Check if the current element (nums[i]) is different from the previous element (nums[i-1]).
            # Since the array is sorted, this indicates a new unique element.
            if nums[i] != nums[i - 1]:
                # If it's a new unique element, place it at the 'k' position.
                nums[k] = nums[i]
                # Move the write pointer forward to prepare for the next unique element.
                k += 1

        # k is the final count of unique elements, and the first k elements of nums
        # now contain the unique numbers.
        print(nums)
        return k



sol = Solution()

# Example 1:
print(sol.removeDuplicates(nums=[1,1,2]))

# Example 2:
print(sol.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))