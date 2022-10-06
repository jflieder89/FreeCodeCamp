"""
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
Update the current existing inventory item quantities (in arr1).
If an item cannot be found, add the new item and quantity into the inventory array.
The returned inventory array should be in alphabetical order by item.
"""
"""
The way it is implied with the test cases if the following:
a) If an item is in the original but not the updating list, the returned list should have the entry from the original as it was
b) If an item is in the updating but not the original list, the returned list should have the entry from the updaring as it was
c) If an item is in both lists, then the returned list should return the summed/combined quantity of that item from both lists
"""
def updateInventory(original_inv, update_inv):
    result = [] #this will be the returned list
    for update_item in update_inv: #iterate through items/lists in the updating list
        flag = False # set a flag to see if the item type in the updated list is found in the original
        for original_item in original_inv: #iterate through items/lists in the current/original list
            if update_item[1] != original_item[1]: # if this item in the updating list is not this item in the original list
                pass
            else:
                flag = True #it is true that there is a match between the original and updating inventories
                result.append([update_item[0] + original_item[0], update_item[1]])
        if flag == False: #if the searched for item in the updating inv is not found anywhere in the original inv
            result.append(update_item)

    for original_item in original_inv: #iterate through items/lists in the original list
        #since the first section catches all items in both lists and all items only in the updating list, now I'll look for items only in the original list
        flag = False # set a flag to see if the item type in the updated list is found in the original
        for update_item in update_inv: #iterate through items/lists in the current/original list
            if original_item[1] != update_item[1]: #if these two are not a match
                pass
            else:
                flag = True #it is true that there is a match between the original and updating inventories
        if flag == False: #if the searched for item in the original inv is not found anywhere in the updating inv
            result.append(original_item)

    #now to sort by the names of the items (second element for each item list). the best way I found to do this is the following:
    def takeSecond(elem):
        return elem[1]
    result.sort(key=takeSecond)
    return result


print(updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))
