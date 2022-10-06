"""
The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both.
For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.
Symmetric difference is a binary operation, which means it operates on only two elements.
So to evaluate an expression involving symmetric differences among three elements (A △ B △ C),
you must complete one operation at a time.
Thus, for sets A and B above, and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.

Create a function that takes two or more arrays and returns an array of their symmetric difference.
The returned array must contain only unique values (no duplicates).
"""
from time import time
start_time = time()
def sym(*args): #go to expcect a variable amount of non-key/value variables, so use *args instead of **kwargs
    diff_lst = [];
    for i in range(len(args) - 1):
        if i == 0: #for the first run through only (to differentiate in case there are more than 2 lists/arguments passed through)
            for elem in args[i]:
                if (elem not in args[i+1]) and (elem not in diff_lst): #if it is not in next list for comparison and is not already in the list of values that only one list has
                    diff_lst.append(elem)
            for elem in args[i+1]:
                if (elem not in args[i]) and (elem not in diff_lst): #if it is not in previous list for comparison and is not already in the list of values that only one list has
                    diff_lst.append(elem)
        if i != 0: #for each need comparison after the first one (if more that 2 lists/arguments are passed through)
            temp_diff_lst = [] #set up a temporary list that diff_lst will be turned into a the end
            for elem in diff_lst:
                if (elem not in args[i+1]) and (elem not in temp_diff_lst): #if it is not in next list for comparison and is not already in the list of values that only one list has
                    temp_diff_lst.append(elem)
            for elem in args[i+1]:
                if (elem not in diff_lst) and (elem not in temp_diff_lst): #if it is not in previous list for comparison and is not already in the list of values that only one list has
                    temp_diff_lst.append(elem)
            diff_lst = temp_diff_lst

    diff_lst.sort()
    return diff_lst

print( sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) )
end_time = time()
print("This took", end_time - start_time, "seconds.")
