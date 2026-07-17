'''
Top-K Most Booked Destinations
Pattern: Heap / Hash Map

Given a list of destination search logs, return the K most frequently searched destinations.

Input:  logs = ["Paris","Rome","Paris","Tokyo","Rome","Paris"], k = 2
Output: ["Paris", "Rome"]
'''
from collections import Counter
import heapq
def Top_k(arr, k):
    counts = Counter(arr)
    return heapq.nlargest(k, counts.keys(), keys=counts.get()
    
