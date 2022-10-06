"""
The next sorting method we'll look at is insertion sort.
This method works by building up a sorted array at the beginning of the list.
It begins the sorted array with the first element.
Then it inspects the next element and swaps it backwards into the sorted array until it is in sorted position.
It continues iterating through the list and swapping new items backwards into the sorted portion until it reaches the end.
This algorithm has quadratic time complexity in the average and worst cases.
Instructions: Write a function insertionSort which takes an array of integers as input and returns an array of these integers in sorted order from least to greatest.
"""
def insertionSort(lst):
    for i in range(1, len(lst)):
        # print()
        # print('lst at the start of the iteration:', lst)
        # print('this is what i starts out as on this iteration:', i)
        # print('lst[i] at the start of the iteration:', lst[i])
        while (lst[i] < lst[i - 1]) and (i > 0):
            # print('here is i in the while loop:', i)
            # print('lst[i] in the while loop:', lst[i])
            # print('lst[i-1] in the while loop:', lst[i-1])
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            # print('here is lst after the swap:', lst)
            i-=1
    return lst

print(insertionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
