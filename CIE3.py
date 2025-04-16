import time

#LINEAR
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
arr = [int(input()) for _ in range(n)]
target = int(input("Enter the search value: "))
found = False
for i in range(n):
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found")

#BINARY
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
arr = [int(input()) for _ in range(n)]
target = int(input("Enter the search value: "))
left, right = 0, n - 1
found = False
while left <= right:
    mid = (left + right) // 2  # Find the middle index
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1  # Search in the right half
    else:
        right = mid - 1  # Search in the left half
if not found:
    print("Element not found")

#BUBBLE
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
arr = [int(input()) for _ in range(n)]
comparisons = 0
swaps = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1
print("Sorted Array using Bubble Sort:", arr)
print(f"Total Comparisons: {comparisons}")
print(f"Total Swaps: {swaps}")

#SELECTION
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
arr = [int(input()) for _ in range(n)]

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array using Selection Sort:", arr)

#MERGE

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid])
    right, right_comparisons = merge_sort(arr[mid:])

    merged, merge_comparisons = merge(left, right)

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged, total_comparisons

def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            merged += [left[i]]
            i += 1
        else:
            merged += [right[j]]
            j += 1
    merged += left[i:] + right[j:]
    return merged, comparisons

n = int(input("Enter the number of elements: "))
print("Enter the elements one by one:")
arr = [int(input()) for _ in range(n)]

start_time = time.time()

sorted_arr, total_comparisons = merge_sort(arr)

end_time = time.time()

execution_time = end_time - start_time

print("Sorted Array using Merge Sort:", sorted_arr)
print(f"Total Comparisons: {total_comparisons}")
print(f"Execution Time: {execution_time:.6f} seconds")