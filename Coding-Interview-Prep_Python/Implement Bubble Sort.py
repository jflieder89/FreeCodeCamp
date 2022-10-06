"""
The bubble sort method starts at the beginning of an unsorted array and 'bubbles up' unsorted values towards the end,
iterating through the array until it is completely sorted.
It does this by comparing adjacent items and swapping them if they are out of order.
The method continues looping through the array until no swaps occur at which point the array is sorted.
This method requires multiple iterations through the array and for average and worst cases has quadratic time complexity.
While simple, it is usually impractical in most situations.
Instructions: Write a function bubbleSort which takes an array of integers as input and returns an array of these integers in sorted order
from least to greatest.
"""
def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
lst1= [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
print(bubbleSort(lst1))
