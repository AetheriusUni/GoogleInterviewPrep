"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. 
For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. 
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""

# function to do the word replacement
def replaceWords(dictionary, sentence):
    # use sets when you want to check if an item is contained within it
    # use lists when you want to iterate over values
    # therefore we use set because it allows us to check if a part of a word is in our set of roots
    rootset = set(dictionary)
    rString = ""

    # for each word in our sentence
    for word in sentence:
        # condition to check if we added a root to the return string already
        # if a root is added already, we check the next word and set added to True
        # if a root is not found, we add the entire word
        added = False
        # for each of the possible roots of a word, from smallest to largest
        for i in range(1, len(word)):
            # if a possible root is seen in the set of roots
            if word[:i] in rootset:
                # append that root to the return string with a space after
                rString+=f"{word[:i]} "
                # set added to True to skip the addition of the entire word
                added = True
                # break to go to the next word
                break
        # if we didn't find a root to add
        if not added:
            # add the entire word to our return string
            rString+=f"{word} "
    # print our return string, but stripping away the extra space after the last word/root we output 
    print(rString.strip())

    
# Main Function
if __name__ == "__main__":
    # input dictionary of roots, not actually a dictionary though 
    dictionary = input().split()
    # sort the dictionary mainly by length, from least to greatest length
    dictionary = sorted(dictionary, key=len)
    print(dictionary)
    # split up the input sentence into a list of words
    sentence = input().split()
    # call the replaceWords function
    replaceWords(dictionary, sentence)
