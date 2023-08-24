from collections import deque
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        # nums1, nums2 = deque(nums1), deque(nums2)
        # Efficient Method => 0(n + m)
        

        # Through 3 Pointers
        l, r, current_index = m - 1, n - 1, m + n - 1
        while r >= 0 and l >= 0:
                nums1[current_index] = max(nums1[l], nums2[r])
                current_index -= 1
                if nums1[l] >= nums2[r]:
                    l -= 1
                else:
                    r -= 1
           
        
        while r >= 0:
             nums1[r] = nums2[r]
             r -= 1
             
        print (nums1)


if __name__ == "__main__":
    sol = Solution()
    sol.merge([1,2,7,8,9,0,0,0],5,[2,5,10],3)
    sol.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3)
    sol.merge([1], 1, [], 0)
    sol.merge([1,5,8,0,0,0,0,0], 3, [-1,2,2,4,6], 5)
    sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)