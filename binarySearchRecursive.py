def binarySearch(arr, target, left, right):
    # just in case left gets bigger than right
    # can happen if the previous step's mid+1 makes left bigger than right
    # or mid-1 makes right smaller than left
    # if either of these cases are true then the target can't exist in our array
    if left > right:
        return False
    
    # get the midpoint index
    mid = (left + right)//2
    # if the value at the midpoint is the target, we return true
    if arr[mid] == target:
        return True
    # if the value of the target is smaller than the midpoint
    elif target < arr[mid]:
        # search the left half of the array
        return binarySearch(arr, target, left, mid-1)
    # if the value of the target is bigger than the midpoint
    else:
        # search the right half of the array
        return binarySearch(arr, target, mid+1, right)

if __name__ == '__main__':
    arr = input().split()
    # convert list to an int list
    arr = list(map(int, arr))
    # binary search only works on sorted arrays
    arr = sorted(arr)
    # value we are searching for
    target = int(input())
    # left-most index
    left = 0
    # right-most index
    right = len(arr)-1
    
    if binarySearch(arr, target, left, right):
        print("Target exists in array")
    else:
        print("Target not in array")
