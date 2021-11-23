'''
Method to sort an array in ascending array using insertion sort algorithm
'''


def insertionSort(arry):
    for i in range(len(arry)):
        # Value that is needed to insert in correct place
        key = arry[i]
        # Current index to compare
        j = i

        # Compare to previous sorted elements
        while j > 0 and key < arry[j-1]:
            arry[j] = arry[j-1]
            j = j-1

        # Update key in correct position
        arry[j] = key

    return arry