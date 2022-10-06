"""
Here we will implement selection sort.
Selection sort works by selecting the minimum value in a list and swapping it with the first value in the list.
It then starts at the second position, selects the smallest value in the remaining list, and swaps it with the second element.
It continues iterating through the list and swapping elements until it reaches the end of the list.
Now the list is sorted. Selection sort has quadratic time complexity in all cases.
Instructions: Write a function selectionSort which takes an array of integers as input and returns an array of these integers in sorted order
from least to greatest.
"""
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # print()
        # print('full lst is:', lst)
        # print('remaining lst is:', lst[i:])
        # print('i is', i)
        min_index = lst[i:].index(min(lst[i:]))
        # print('min_index is', min_index)
        # print('min_index elem in remaining is:', lst[min_index + 1])
        if min_index != i:
            #print('Making a switch!')
            lst[i], lst[min_index + i] = lst[min_index + i], lst[i]
        #print('lst is:', lst)
    return lst

lst1 =[1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]
lst2 = [3,2,1]
print(selectionSort(lst1))
