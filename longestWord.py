import re

def LongestWord(sen):
    high = ''
    # code goes here
    words = re.split('\W+', sen)
    print(words)
    for word in words:
        if len(word)>len(high):
            high = word
    sen = high
    return sen

# keep this function call here 
if __name__ == '__main__':
    n = input()
    print(LongestWord(n))
