def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Find the actual minimum in the remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage:
data = [64, 25, 12, 22, 11]
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)
