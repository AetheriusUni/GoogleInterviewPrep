def FirstReverse(strParam):
    swapIndex = len(strParam)-1
    if swapIndex == 0:
        return strParam
    sList = list(strParam)
    # code goes here
    for i in range(0, len(strParam)//2):
        sList[i], sList[swapIndex] = sList[swapIndex], sList[i]
        swapIndex-=1
    strParam = ''.join(sList)
    return strParam

if __name__ == '__main__':
    inString = input()
    print(FirstReverse(inString))
