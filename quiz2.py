import random
import time

def generate_random_numbers(n, seed=42):
    random.seed(seed)
    return [random.randint(0, 100) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    return sorted_arr, end_time - start_time

def main():
    n = 50
    numbers = generate_random_numbers(n)
    
    print("Original array:", numbers)
    
    # Bubble Sort
    bubble_sorted, bubble_time = measure_time(bubble_sort, numbers)
    print("\nBubble Sort:")
    print("Sorted array:", bubble_sorted)
    print("Time taken:", bubble_time, "seconds")
    
    # Merge Sort
    merge_sorted, merge_time = measure_time(merge_sort, numbers)
    print("\nMerge Sort:")
    print("Sorted array:", merge_sorted)
    print("Time taken:", merge_time, "seconds")
    
    print("\nBest Case Analysis:")
    print("Bubble Sort: O(n) - When the array is already sorted")
    print("Merge Sort: O(n log n) - Regardless of the input array")

if __name__ == "__main__":
    main()