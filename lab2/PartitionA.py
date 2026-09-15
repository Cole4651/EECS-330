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
    pivot_index = low

    # Step 1: Select the pivot
    # pivot = arr[high]

    # Step 2: Create a temporary array
    # temp = [0] * (high - low + 1)

    # Step 3: Initialize the index for the temp array
    # idx = 0

    # Step 4: Place all values <= pivot in the left portion of temp
    for i in range(low, high):
        if arr[i] <= pivot:
            temp[idx] = arr[i]
            idx += 1

    # Step 5: Record the pivot position in the temp array
    pivot_index = idx
    temp[idx] = pivot
    idx += 1

    # Step 6: Place all values > pivot in the right portion of temp
    for i in range(low, high):
        if arr[i] > pivot:
            temp[idx] = arr[i]
            idx += 1

    # Step 7: Put the values back into the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    # Step 8: Return the pivot index
    return pivot_index


# Quick test
arr = [8, 3, 6, 2, 7, 5, 1, 4]
result = partition(arr, 0, len(arr) - 1)
print("Partitioned array:", arr)
print("Pivot index:", result)
