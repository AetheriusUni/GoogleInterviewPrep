def hasPairWithSum(s, q):
    # stores the values that, when added to a number we've already seen, will give us the sum we're looking for
    compliments = set()
    # for each of the values in our list q
    for i in range(len(q)):
        # if the current value we're looking at is a compliment to one of the numbers we've seen before
        if q[i] in compliments:
            # then that means that that value and some previous value make a pair that add up to the sum we want, meaning we can return True
            return True
        # we add the difference between the sum and the current value we're looking at (gives us the "compliment")
        # storing this in the compliments set allows us to check if a value we're looking at can make a pair with a previously seen value in q
        compliments.add(s-q[i])
    return False

if __name__ == '__main__':
    # sum we are looking for
    s = int(input())
    # list of numbers we're looking at
    q = list(map(int, input().rstrip().split()))
    # NOTE: The below line is only needed if our input is an unordered list; hasPairWithSums only works with ordered lists
    # q.sort()
    # for debugging, making sure that the line above actualy properly makes a list as intended -> it's working as intended
    # print(q)
    print(hasPairWithSum(s, q))
    
