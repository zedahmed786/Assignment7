def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Get the input array from the user
input_str = input("Enter the array of integers (separated by spaces): ")
input_array = list(map(int, input_str.split()))

# Sort the input array
sorted_array = sorted(input_array)

# Print the sorted array
print("Sorted array:", sorted_array)

# Get the element to search from the user
target = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(sorted_array, target)

if index != -1:
    # Count the number of occurrences of the element
    count = sorted_array.count(target)
    print("Number of occurrences of element", target, "is:", count)
else:
    print("Element", target, "not found in the array.")
