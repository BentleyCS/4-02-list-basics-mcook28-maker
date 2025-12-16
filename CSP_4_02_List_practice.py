
def bookends(li: list):

    """
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
    """
    ends = []
    count = 0
    while count < 2:
        if count == 0:
            first_val = li.pop(0)
            ends.append(first_val)
        else:
            last_val = li.pop(-1)
            ends.append(last_val)
        count += 1
    return ends
nums = [60,5,8,3,5]
result = bookends(nums)
print("Removed:", result)
print("Remaining:", nums)
def inOrder(li : list):
    """Given a list of numbers return True if the list is in ascending order."""
    for i in range(len(li) - 1):
        # If any element is bigger than the one after it,
        # the list is NOT in ascending order.
        if li[i] > li[i + 1]:
            return False
    return True
print(inOrder([3, 1, 4]))
def find(li: list, target : int):
    for i in range(len(li)):      # loop through all indexes
        if li[i] == target:       # check if value matches
            return i              # return the index immediately
    return -1                     # not found
print(find([1, 3, 5, 7, 9], 3))
def removeLowest(li):
    """
      Removes ONE instance of the lowest number in the list.
      """

    # assume first value is the lowest
    lowest = li[0]

    # loop to find the lowest value
    for i in range(len(li)):
        if li[i] < lowest:
            lowest = li[i]

    # remove one occurrence of the lowest value
    li.remove(lowest)


# --- PRINT TEST ---
nums = [3, 6, 7, 2, 12]
removeLowest(nums)
print(nums)  # [3, 6, 7, 12]
def keepOrder(li: list, value):
    """
    Inserts value into the correct position so the list stays in ascending order.
    """

    for i in range(len(li)):
        if value < li[i]:
            li.insert(i, value)
            return

    # if value is greater than all elements, add to the end
    li.append(value)


# --- PRINT TEST ---
arr = [1, 3, 5, 6]
keepOrder(arr, 4)
print(arr)   # [1, 3, 4, 5, 6]
def merge(l1:list, l2:list):
    """
       Merges two sorted lists into a new sorted list.
       Original lists are not modified.
       """

    merged = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # add remaining elements
    while i < len(l1):
        merged.append(l1[i])
        i += 1

    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged

# --- PRINT TEST ---
print(merge([1, 3, 5], [2, 4, 6, 8]))
# [1, 2, 3, 4, 5, 6, 8]