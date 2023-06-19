def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Get the input array from the user
input_str = input("Enter the array of integers (separated by spaces): ")
input_array = list(map(int, input_str.split()))

# Remove duplicates from the array
unique_array = remove_duplicates(input_array)

# Sort the array using selection sort
selection_sorted_array = selection_sort(unique_array)

# Sort the array using bubble sort
bubble_sorted_array = bubble_sort(unique_array)

# Print the sorted arrays
print("Sorted array (Selection Sort):", selection_sorted_array)
print("Sorted array (Bubble Sort):", bubble_sorted_array)
