def subtractProductAndSum(n):
    product = 1
    sum = 0
    numSplit = str(n)

    for num in numSplit:
        product*=int(num)
        sum+=int(num)

    return product - sum

if __name__ == '__main__':
    n = int(input())
    print(subtractProductAndSum(n))
