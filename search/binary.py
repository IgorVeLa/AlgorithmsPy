'''
Method to find a value using binary search algorithm using recursion
Includes other methods such as insert and deleting values using binary search algorithm
'''


def binarySearch(arry, searchValue, L, R):
    # If right pointer is less than left pointer then it's been recursively called to the point where all values have
    # been compared
    if R < L:
        return f'{searchValue} was not found in {arry}'

    # Find mid point in the array
    m = int((L + R) / 2)

    # Search value is the midpoint
    if searchValue == arry[m]:
        return f'{searchValue} was found in {arry}'
    # When search value is greater than midpoint
    if searchValue > arry[m]:
        # Searches right half of the array
        return binarySearch(arry, searchValue, m+1, R)
    # When search value is less than midpoint
    else:
        # Searches left half of the array
        return binarySearch(arry, searchValue, L, m-1)