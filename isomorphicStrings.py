"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

def isIsomorphic(s, t):
    sMap = {}
    tMap = {}
    # zip allows us to iterate through both items in multiple lists while keeping them both in scope of the loop
    # c1 in s; c2 in t
    for c1, c2 in zip(s, t):
        # if we didn't map a value yet, we map it
        # sMap gets key c1 with value c2, effectively assigning a "match" of c1 and c2
        # tMap is the same way
        if c1 not in sMap and c2 not in tMap:
            sMap[c1] = c2
            tMap[c2] = c1
        # if sMap value at key c1 isn't the same as the value c2, then there is a mismatch; same for tMap
        # we are comparing the values we are iterating over to the values we already have mapped
        # ex sMap(c1) = a, but right now c2 = b -> since this is trying to do a different mapping AKA not isomorphic
        elif sMap.get(c1) != c2 or tMap.get(c2) != c1:
            # since there's a mismatch we don't have an isomorphic so we return false
            return False
    # everything looks good so we return true
    return True

if __name__ == '__main__':
    s = input()
    t = input()
    print(isIsomorphic(s, t))
