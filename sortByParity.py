"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

ANSWER EXPLANATION: Since I'm allowed to return any of the arrays, I don't care about sorting of any sort aside from the first half of the list being even and the next half being odd.
To run in linear time I have a left index lIndex for adding even numbers to the earliest part of the return list (increments when I add an even value)
I have a right index rIndex for adding odd numbers to the latest part of the return list (decrements each time an odd value)
"""

def sortArrayByParity(nums):
    # initialize set size empty list
    rList = [None]*len(nums)
    lIndex = 0
    rIndex = len(nums)-1
    # for each value in lst
    for i in range(len(nums)):
        # put all the even numbers first
        if nums[i]%2==0:
            rList[lIndex]=nums[i]
            lIndex+=1
        # add odds at the end of the list
        else:
            rList[rIndex]=nums[i]
            rIndex-=1

    return rList

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    lst = []

    for i in range(n):
        ele = int(input())
        lst.append(ele)
    
    print(sortArrayByParity(lst))
