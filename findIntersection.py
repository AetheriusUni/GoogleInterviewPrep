"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, 
the second element will represent a second list of comma-separated numbers (also sorted). 
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
If there is no intersection, return the string false.

Example input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13

INTERSECTIONS ARE THE NUMBERS THAT EXIST IN BOTH LISTS
"""

import re

def FindIntersection(strArr):

    # split the strings into 2 separate lists
    # delimiter is comma and whitespace
    aArr = re.split('\W+', strArr[0])
    bArr = re.split('\W+', strArr[1])
    rList = []
    aArr = list(map(int, aArr))
    bArr = list(map(int, bArr))
    # sort both of the lists
    aArr = sorted(aArr)
    bArr = sorted(bArr)
    # for each of the indices in aArr
    for i in range(len(aArr)):
        # check if the value has been seen in bArr
        for j in range(len(bArr)):
            # this condition ends the search through bArr early if there is no chance of bArr having an intersection with aArr
            if aArr[i] < bArr[j]:
                break
            # if an intersection exists
            elif aArr[i]==bArr[j]:
                # append them to the return list
                rList.append(aArr[i])
    strArr = rList
    return strArr

# keep this function call here 
# print(FindIntersection(input()))
if __name__ == '__main__':
    #testcase1
    #aString = "1, 3, 4, 7, 13"
    #bString = "1, 2, 4, 13, 15"
    #testcase2
    aString = "1, 3, 9, 10, 17, 18"
    bString = "1, 4, 9, 10"
    strArr = []
    strArr.append(aString)
    strArr.append(bString)
    print(FindIntersection(strArr))
