'''
Cheapest Discounted Stay
Pattern: Sliding Window / Array

Given daily room prices for the next N days and a required minimum stay length k, find the cheapest total cost for any consecutive k-day stay.

Input: prices = [120, 100, 90, 150, 80, 95], k = 3
Output: 265  # days 3-5 (indices 2..4): 90+150+80=320... check window with min sum
'''
import deque
def cheapest_stay(prices, k):
    window = deque()
    window_sum = 0
    min_sum = 0
    min_start = 0
    min_end = 0
    
    for i in range(k):        # build the first window
        window.append(prices[i])
        window_sum = window_sum + prices[i]
    min_sum = window_sum
    min_start = 0             # first window starts at index 0

    # slide: add new day at the back, remove oldest day from the front
    start = 1            # start index of the *next* window we'll form
    for i in range(k, len(prices)):
        window.append(prices[i])
        removed = window.popleft()
        window_sum = window_sum - removed
        if min_sum > window_sum:
            min_sum = window_sum
            min_start = start
        start = start + 1
    min_end = min_start + k -1
        
    return (min_sum, min_start, min_end)
