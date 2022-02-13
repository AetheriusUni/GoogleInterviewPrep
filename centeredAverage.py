"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. 
Input Constraint: You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 (as a float the answer should have been 5.2, so the return value is stil an int)
centered_average([-10, -4, -2, -4, -2, 0]) → -3
^ based on these test cases we can assume that return values remain as integers
"""

def centered_average(nums):
    rVal = 0
    # sort nums list so it's easy to remove the first and last elements
    nums = sorted(nums)
    # for each of the elements that aren't the first or last elements
    for i in range(1, len(nums)-1):
        # add them up
        rVal+=nums[i]
    # now we divide by the amount of remaining values to find the mean
    rVal//=len(nums)-2

    return rVal

if __name__ == '__main__':

    n = int(input("Enter number of elements : "))
    inArr = []
    for i in range(0, n):
        ele = int(input())
        inArr.append(ele)
    print(centered_average(inArr))
