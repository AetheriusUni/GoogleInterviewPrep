def binarySearch(arr, target):
    # left-most index
    left = 0
    # right-most index
    right = len(arr)-1

    # while we can still possibly find the target
    # if left is greater than right, that means we have searched the entire list
    while left <= right:
        # midpoint formula
        mid = (left + right)//2
        # if the midpoint value is the target we return True
        if arr[mid] == target:
            return True
        # if the target is less than the midpoint value
        elif target < arr[mid]:
            # the upper limit of what we search becomes the midpoint minus 1 AKA search the left side only
            right = mid - 1
        # if the target is greater than the midpoint value
        else:
            # the lower limit of what we search becomes the index of the midpoint plus 1 AKA search the right side only
            left = mid + 1
    # couldn't find the target after the binary search, so we return false
    return False

if __name__ == '__main__':
    arr = input().split()
    # convert list to an int list
    arr = list(map(int, arr))
    # binary search only works on sorted arrays
    arr = sorted(arr)
    # value we are searching for
    target = int(input())
    
    if binarySearch(arr, target):
        print("Target exists in array")
    else:
        print("Target not in array")
