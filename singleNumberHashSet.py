"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

ANSAWER REASONING: since we know every other element appears twice
if we don't see that a value is in the hashset we add it
otherwise we can remove the value already stored in the hashset
this solution wouldn't work if there were to be more than 2 instances of duplicates for any value

this leaves us with the one non-duplicated remaining in the hashset
"""

def singleNumber(nums):

    hashset = set()
    # for each of the values
    for num in nums:
        # if it's not in the hashset yet
        if num not in hashset:
            # add it to the hashset
            hashset.add(num)
        # otherwise
        else:
            # take the value out of the hashset
            hashset.remove(num)
    
    # set return vavlue to the only remaining value in the hashset
    # idk how else to return the one value without iterating
    for i in hashset:
        return i
        

if __name__ == '__main__':
    n = int(input())
    aList = []

    for i in range(n):
        ele = int(input())
        aList.append(ele)
    print(singleNumber(aList))
