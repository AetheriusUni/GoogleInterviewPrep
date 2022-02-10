def FirstFactorial(num):
    # factorial of 0 and 1 is 1, so we return 1 for those cases
    if num <= 1:
        return 1
    else:
        # count is the number we multiply num by 
        count = num-1
        # while count is greater than 1
        # ex. if num = 7, this loop will run for count values from 6 down to 2
        # this gives us 7*6*5*4*3*2 and we don't need to multiply by 1 since the num doesn't change
        while count > 1:
            # num = num*count
            num*=count
            # decrement count so the next time we do multiplication it's with the next value
            # ex. if we just went through this loop with count = 5, next loop will be count = 4 and so on
            count-=1
    return num

if __name__ == '__main__':
    num = int(input())
    print(FirstFactorial(num))
