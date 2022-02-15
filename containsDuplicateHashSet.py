def containsDuplicate(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)
    return False

if __name__ == '__main__':
    n = int(input())
    aList = []
    for i in range(n):
        ele = int(input())
        aList.append(ele)
    print(containsDuplicate(aList))
