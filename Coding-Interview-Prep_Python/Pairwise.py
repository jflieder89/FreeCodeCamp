"""
Given an array arr, find element pairs whose sum equal the second argument arg and return the sum of their indices.
You may use multiple pairs that have the same numeric elements but different indices.
Each pair should use the lowest possible available indices. Once an element has been used it cannot be reused to pair with another element.
For instance, pairwise([1, 1, 2], 3) creates a pair [2, 1] using the 1 at index 0 rather than the 1 at index 1, because 0+2 < 1+2.
For example pairwise([7, 9, 11, 13, 15], 20) returns 6.
The pairs that sum to 20 are [7, 13] and [9, 11]. We can then write out the array with their indices and values.
Below we'll take their corresponding indices and add them.
7 + 13 = 20 → Indices 0 + 3 = 3
9 + 11 = 20 → Indices 1 + 2 = 3
3 + 3 = 6 → Return 6
"""
"""
#first solution I came up with:
def pairwise(lst, target):
    result = 0 #to be returned at the end of calculations
    used_elements = []# create a list of element indicies to not use a second time
    for i in range(len(lst)): #iterate through the elements of the passed list a first time
        #print('i is :', i)
        if i in used_elements: #if the i element was already used while it was a j element to make an applicable match
            continue
        flag = False #false if a match with elem i has not yet been found and still searching/comparing with j elements
        while flag == False:
            for j in range(len(lst)): #iterate through the elements of the passed list a second time
                if j in used_elements: #if the j elements was already used while it was an i element to make an applicable match
                    continue
                if (flag == True): #break out if a match was found, so the same element i isn't used again
                    break
                # print('i is :', i, 'and j is :', j, 'and flag is', flag)
                if i == j: #want to exlude possibility of using the same list element twice
                    #print('Looking at same element twice. Going to continue')
                    continue #go to the next j
                if lst[i] + lst[j] == target: #if we have a match!
                    # print('Match! i is :', i, 'and j is :', j)
                    flag = True
                    result += i
                    result += j
                    used_elements.append(i)
                    used_elements.append(j)
            flag = True #set flag to True if I make it through all j's without an applicable match
    return result
#end of first solution I came up with
"""
#second solution, trying to be more streamlined:
def pairwise(lst, target):
    result = 0 #to be returned at the end of calculations
    used_elements = []; # create a list of element indicies to not use a second time
    for i in range(len(lst)): #iterate through the elements of the passed list a first time
        if i in used_elements: #if the i element was already used while it was a j element to make an applicable match
            continue
        for j in range(len(lst)):#iterate through the elements of the passed list a second time
            if (j in used_elements) or (i == j): #if the j element was already used while it was an i element to make an applicable match, or if we're using the same element twice
                continue
            if lst[i] + lst[j] == target: #if we have a match!
                result += i
                result += j
                used_elements.append(i)
                used_elements.append(j)
                break #only breaks out of the inner j loop, not the i loop!
    return result
#end of second solution
x = pairwise([], 100)
print(x)
