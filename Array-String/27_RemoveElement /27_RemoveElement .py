from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        my solution:
        This code repeatedly removes all occurrences of val from the list nums.
	    The while val in nums: condition checks if the value val is still present in the list.
	    Inside the loop, nums.remove(val) deletes the first occurrence of val in the list.
	    This process continues until there are no more occurrences of val left in the list.

        """
        while val in nums:
            nums.remove(val)

        # It's not efficient because of the time complexity of sort(). This code's complexity is Big O of n squared (or Big O of n to the power of two)

        """
        better solution:
        “This code removes all occurrences of val from the list nums in-place and returns the count of elements that are not equal to val.
	    i = 0 initializes a pointer i that keeps track of the position where the next non-val element should be placed.
	    for num in nums: iterates through each element num in the list.
	    if num != val: checks whether the current element is not equal to val.
	    If so, nums[i] = num copies the current element to the i-th position in the list.
	    i += 1 increments the pointer to the next position.
	    After the loop, return i returns the number of elements that are not equal to val.”
        """
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
                print("nums : ", nums)

        return i



sol = Solution()

# Example 1:
sol.removeElement(nums=[3,2,2,3], val= 3)

# Example 2:
sol.removeElement(nums=[0,1,2,2,3,0,4,2], val= 2)