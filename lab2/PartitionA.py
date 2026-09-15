def partition(arr, low, high):
    """
    Partition the subarray arr[low..high] using the last element as the pivot.
    This version follows the assignment steps and uses a temporary array
    rather than swapping elements in place.

    Args:
        arr (list): list to partition
        low (int): starting index of the current subarray
        high (int): ending index of the current subarray

    Returns:
        int: the final index of the pivot after partitioning
    """
    pivot = arr[high]
    temp = [0] * (high - low + 1)
    idx = 0

    # Step 1: Select the pivot
    # pivot = arr[high]

    # Step 2: Create a temporary array
    # temp = [0] * (high - low + 1)

    # Step 3: Initialize the index for the temp array
    # idx = 0

    # Step 4: Put all values <= pivot on the left side of temp
    for i in range(low, high):
        if arr[i] <= pivot:
            temp[idx] = arr[i]
            idx += 1

    # Step 5: Record the pivot position
    pivot_index = idx
    temp[idx] = pivot
    idx += 1

    # Step 6: Put all values > pivot on the right side of temp
    for i in range(low, high):
        if arr[i] > pivot:
            temp[idx] = arr[i]
            idx += 1

    # Step 7: Copy temp back into the array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    # Step 8: Return the pivot index
    return pivot_index


# Quick test
arr = [8, 3, 6, 2, 7, 5, 1, 4]
final_index = partition(arr, 0, len(arr) - 1)

left_part = arr[:final_index]
right_part = arr[final_index + 1:]
pivot_value = arr[final_index]

print("The pivot index is:", final_index)
print("The pivot value is:", pivot_value)
print("The left part is:", left_part)
print("The right part is:", right_part)
