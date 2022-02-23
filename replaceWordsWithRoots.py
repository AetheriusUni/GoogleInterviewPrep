class Solution:
    def replaceWords(self, roots, sentence):
        # hashset of roots
        rootset = set(roots)

        def replace(word):
            # for each of the chars in a word
            for i in range(1, len(word)):
                # check if the string created by the first i chars is in the rootset
                if word[:i] in rootset:
                    # return the string that was found if any
                    return word[:i]
            # if there was nothing found among the rootset, we just return the input word itself
            return word
        # returns a string composed of our replaced words
        # we join our list of strings to the blank string which is created using--
        # map(replace, sentence.split())) takes each word from the split sentence as an argument to our replace function

        return " ".join(map(replace, sentence.split()))
