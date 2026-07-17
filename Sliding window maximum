'''
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        output = []
        l = r = 0
        while r<len(nums):
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()
            dq.append(r)
            if dq[0]<l:
                dq.popleft()
            if (r+1)>=k:
                output.append(nums[dq[0]])
                l = l+1
            r = r+1
        return output
