def CountingSortIntegers(arr):
    # Determine the range of the array values
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    # Create count array with size equal to the range of elements
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store count of each integer
    for num in arr:
        count[num - min_val] += 1

    # Modify the count array such that each index will store the sum till previous step
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):  # reverse to maintain stability, if needed
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Example to test the adapted algorithm
arr = [40, 15, 9, 92, 14, 2, -21, -2, 39, 44]
sorted_arr = CountingSortIntegers(arr)
print("Sorted Array:", sorted_arr)


#==============
#Task 1- D
def CountingSort(arr):
    # Find the maximum and minimum elements to determine the range
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize the count array and the output array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Adjust the count array to store cumulative counts
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the output array using the count array
    for num in reversed(arr):  # reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
# Test array of 20 distinct elements
test_array = [34, 7, 23, -4, 5, 93, -18, 23, 42, 57, 24, 12, 9, -31, 45, 67, -28, 73, -8, 90]
sorted_array = CountingSort(test_array)
print("Sorted Array:", sorted_array)


#Task 1 -D

def CountingSortNonDistinct(arr):
    if not arr:
        return arr

    # Find the maximum and minimum elements to determine the range
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize the count array and the output array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Adjust the count array to store cumulative counts
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the output array using the count array, modified for duplicates
    for num in reversed(arr):  # reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
# Test array with duplicate elements
test_array = [34, 7, 23, 23, 5, 93, -18, 23, 42, 57, 24, 12, 9, -31, 45, 67, 23, 73, -8, 90]
sorted_array = CountingSortNonDistinct(test_array)
print("Sorted Array with Duplicates:", sorted_array)
