def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to optimize the algorithm by stopping if no swaps occur in a pass
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage
input_array = [5, 2, 9, 1, 5, 6]
bubble_sort(input_array)
print("Sorted array:", input_array)
