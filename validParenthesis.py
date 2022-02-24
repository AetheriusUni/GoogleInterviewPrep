class Solution:
    def isValid(self, s: str) -> bool:
        # bracket pair dictionary, assign right brackets as values for left bracket keys
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        # list for left brackets that still need to be closed, will be used as a queue
        waiting_close = []
        # for each character in our string
        for char in s:
            # makes solution more general if we were to have non-bracket characters in string
            # allows us to only put in right brackets that need closing into the waiting_close queue
            need_close = bracket_pairs.get(char)
            # if we find that we are on a bracket that needs a matching left bracket
            if need_close:
                # we add that bracket to the queue
                waiting_close.append(need_close)
            # if the first bracket is a right bracket
            # or the current char isn't the matching bracket for the last added value to waiting_close
            elif not waiting_close or char != waiting_close.pop():
                return False

        return len(waiting_close) == 0
    
    #INPUT ([{(}])
    #NEED CLOSE )]}) 
    #WAITING CLOSE )]})
    # when we get to char } it's not equal to the popped value of waiting_close which is ) so we return false
