'''
Merge Overlapping Reservations

Pattern: Intervals / Sorting
A property has a list of bookings, each [check_in, check_out] (integers representing days). Merge all overlapping or touching bookings into consolidated occupied ranges.

Input:  [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
'''

def merge_bookings(bookings):
    if not bookings:
        return []
    bookings.sort(key = lambda x : x[0])
    merged = [bookings[0]]
    for start, end in booking[1:]:
        last_end = merged[-1][1]
        if start<=last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start,end])
    return merged

'''
Edge cases
1. Empty input
python if not bookings:
    return []
Handled explicitly, first line. Without this, bookings[0] on the next line would crash with an IndexError. 
2. Single element
pythonbookings = [[5, 8]]
merged = [bookings[0]] → merged = [[5,8]]. The loop for start, end in bookings[1:] runs zero times, since there's nothing after the first element. Function returns [[5,8]] — correct, and it required no special-casing because the code naturally degrades to "just the seed value."
3. Overlapping boundaries (touching, not just overlapping)
pythonbookings = [[1, 3], [3, 5]]
Is 3 <= 3? Yes. These merge into [1, 5], even though one ends exactly where the other begins. 
pythonbookings = [[1, 10], [2, 3]]
merged[-1][1] = max(last_end, end) → max(10, 3) = 10. Without the max(), you'd shrink the range and silently produce wrong output.
'''
