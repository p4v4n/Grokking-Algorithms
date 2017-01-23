# Binary Search in a Sorted List.


def binary_search(Li, item):

    low, high = 0, len(Li) - 1

    while low <= high:
        mid = (low + high)//2
        guess = Li[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
