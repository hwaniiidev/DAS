from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        my solution:
        This code first takes the first m elements of nums1 (which are the valid elements to be merged) and concatenates them with all elements of nums2.
        The resulting list replaces the original nums1 in-place.
        Finally, the combined list is sorted in non-decreasing order using Python’s built-in sort() method.
        """
        nums1[:] = nums1[:m] + nums2
        nums1.sort()
        print("answer : ", nums1[:])
        # It's not efficient because of the time complexity of sort()


        """
        better solution:
        This code merges two sorted arrays, nums1 and nums2, into a single sorted array in-place.
        It uses three pointers: p1 pointing to the last valid element of nums1, p2 pointing to the last element of nums2, and p pointing to the last index of nums1 (which has extra space to accommodate nums2).
        The algorithm compares elements from the end of both arrays and fills nums1 from the back, placing the larger element at index p.
        After one of the arrays is exhausted, any remaining elements from nums2 are copied to nums1.
        This approach ensures the final nums1 array is sorted without using extra space and operates in O(m+n) time.
        """
        # Initialize pointers
        p1 = m - 1  # Last valid element index in nums1
        p2 = n - 1  # Last element index in nums2
        p = m + n - 1  # Last index of nums1



        # Fill num1 from the end
        while p1 >= 0 and p2 >= 0:
            print(p1, p2, p)
            print(nums1[p1], nums2[p2])
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            print("nums1 : ", nums1[:])
            print()


        # If there are remaining elements in num2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
            print("nums1 : ", nums1[:])
            print()

        print("answer : ", nums1[:])


sol = Solution()

# Example 1:
sol.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
print("expected: ", [1,2,2,3,5,6])

sol.merge(nums1=[1], m=1, nums2=[], n=0)
print("expected: ", [1])

sol.merge(nums1=[0], m=0, nums2=[1], n=1)
print("expected: ", [1])