import collections

def groupAnagrams(strs):
    # you can't store lists in a hashmap, so we have to use defaultdict that stores type list
    ans = collections.defaultdict(list)
    # for each of the strings that was input
    for s in strs:
        # append string to the list at key = sorted string
        ans[tuple(sorted(s))].append(s)
    # then miraculously easy enough that's it
    return ans.values()
    

if __name__ == '__main__':
    n = int(input())
    strList = []
    for i in range(n):
        ele = input()
        strList.append(ele)

    print(groupAnagrams(strList))
