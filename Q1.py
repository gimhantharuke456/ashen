def counting_sort(A):
    n = len(A)
    C = [0] * n
    B = [0] * n

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                C[i] += 1

    for i in range(n):
        B[C[i]] = A[i]

    return B


# Testing the algorithm
A = [40, 15, 9, 92, 14, 2, -21, -2, 39, 44]
sorted_array = counting_sort(A)
print("Sorted array:", sorted_array)

def counting_sort_with_duplicates(arr):
    # Find the maximum and minimum elements in the array
    max_element = max(arr)
    min_element = min(arr)

    # Calculate the range of elements
    range_of_elements = max_element - min_element + 1

    # Initialize the count array with zeros
    count = [0] * range_of_elements

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num - min_element] += 1

    # Modify the count array to store the actual position of each element in the sorted array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create the sorted array using the count array
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count[num - min_element] - 1] = num
        count[num - min_element] -= 1

    return sorted_arr


# Test the counting_sort_with_duplicates function
arr = [40, 15, 3, 27, 14, 3, -21, 3, 27, 44]
sorted_arr = counting_sort_with_duplicates(arr)
print("Original Array:", arr)
print("Sorted Array:", sorted_arr)

