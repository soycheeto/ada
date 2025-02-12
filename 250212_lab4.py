"""
array = [5,7,9,15,3]
normal: return largest
activity: return smallest
"""

def largest(brr):
    largest = brr[0]
    for i in brr:
        if i > largest:
            largest = i
    return largest

def smallest(brr):
    smallest = brr[0]
    for i in brr:
        if i < smallest:
            smallest = i
    return smallest
print(largest([5,7,9,15,3]))
print(smallest([5,7,9,15,3]))

