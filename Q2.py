import random
import time

# Sorting algorithms
def selection_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

def insertion_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons

def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        comparisons += merge_sort(L)
        comparisons += merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return comparisons

def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return comparisons
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    comparisons += len(arr) - 1
    return comparisons + quick_sort(left) + quick_sort(right)

def heapify(arr, n, i):
    comparisons = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += 1
        comparisons += heapify(arr, n, largest)

    return comparisons

def heap_sort(arr):
    comparisons = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        comparisons += 1
        comparisons += heapify(arr, i, 0)

    return comparisons

def counting_sort(arr):
    comparisons = 0
    n = len(arr)
    output = [0] * n
    count = [0] * (max(arr) + 1)

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    return comparisons

# Main menu
def main_menu():
    print("Main Menu:")
    print("1. Test an individual sorting algorithm")
    print("2. Test multiple sorting algorithms")
    print("3. Exit")

def individual_menu():
    print("Individual Sorting Algorithm Menu:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")
    print("6. Counting Sort")

def generate_array(size):
    return [random.randint(0, 100) for _ in range(size)]

def test_algorithm(algorithm, arr):
    start_time = time.time()
    comparisons = algorithm(arr)
    end_time = time.time()
    print("Sorted Array:", arr)
    print("Number of Comparisons:", comparisons)
    print("Time taken:", end_time - start_time, "seconds")

def test_individual_algorithm():
    individual_menu()
    choice = int(input("Enter your choice: "))
    size = int(input("Enter the size of the array: "))
    arr = generate_array(size)
    print("Original Array:", arr)
    if choice == 1:
        test_algorithm(selection_sort, arr)
    elif choice == 2:
        test_algorithm(insertion_sort, arr)
    elif choice == 3:
        test_algorithm(merge_sort, arr)
    elif choice == 4:
        test_algorithm(quick_sort, arr)
    elif choice == 5:
        test_algorithm(heap_sort, arr)
    elif choice == 6:
        test_algorithm(counting_sort, arr)

def test_multiple_algorithms():
    size = int(input("Enter the size of the array: "))
    arr = generate_array(size)
    print("Original Array:", arr)

    algorithms = [
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort)
    ]

    print("\nSorting algorithm name\tArray size\tNum. of Comparisons\tRun time (in ms.)")

    for algorithm_name, algorithm in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        comparisons = algorithm(arr_copy)
        end_time = time.time()
        run_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"{algorithm_name}\t\t\t{size}\t\t{comparisons}\t\t\t{run_time:.2f} (ms)")


# Main function
if __name__ == "__main__":
    while True:
        main_menu()
        option = int(input("Enter your choice: "))
        if option == 1:
            test_individual_algorithm()
        elif option == 2:
            test_multiple_algorithms()
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

