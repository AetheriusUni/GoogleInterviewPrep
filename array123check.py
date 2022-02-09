"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""


def array123(nums):
    # for index, value in nums -- note: can use for i in range(len(nums)) and the problem is solved the same way
    
    for i, num in enumerate(nums):
        if i + 2 < len(nums) and num == 1:
            if nums[i+1]==2 and nums[i+2]==3:
                return True
    """
    for i in range(len(nums)):
        if i + 2 < len(nums) and nums[i] == 1:
            if nums[i+1]==2 and nums[i+2]==3:
                return True
    """
    
    return False

if __name__ == '__main__':
    n = int(input())
    #nums = []
    #for i in range (n):
        #ele = int(input())
        #nums.append(ele)
    # make a list by mapping int values from input by first removing extra white spaces, then splitting values on whitespace
    # aka can accept inputs like "  1 3   6  4 2"
    # after strip: "1 3 6 4 2"
    # after split: "[1, 3, 6, 4, 2]"
    nums = list(map(int, input("\nEnter the list: ").strip().split()))[:n]
    #print(nums)
    print(array123(nums))
