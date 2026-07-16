'''
Valid Booking Reference Code

Pattern: Stack

A booking reference string uses brackets ()[]{} to represent nested add-ons (e.g., a room booking containing a nested breakfast package containing a nested late-checkout option). Determine if the bracket sequence is valid.

Input:  "(a[b]{c})"
Output: True
'''
def is_valid_reference(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
