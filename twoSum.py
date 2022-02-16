"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    hashmap = {}

    # populate hashmap
    for i in range(len(nums)):
        # get the complement of that number that adds up to target
        complement = target - nums[i]
        # if we've already seen it in the hashmap
        if complement in hashmap:
            # we return the pair of our current index and the
            # index of the complement, which is stored as a VALUE in hashmap
            return [i, hashmap[complement]]
        # if we're not done, we add nums[i] to hashmap,
        # but with nums[i] being the key and i being the value
        # this is so we're able to easily obtain index i later
        hashmap[nums[i]] = i

if __name__ == '__main__':
    n = int(input())
    target = int(input())
    aList = []
    for i in range(n):
        ele = int(input())
        aList.append(ele)

    print(twoSum(aList, target))
