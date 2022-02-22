# your task is to complete this function
# function should return false/0 if length is even
# else return true/1
def isLengthEvenOrOdd(head):
    # Code here
    currentNode = head
    count = 0
    while currentNode:
        currentNode = currentNode.next
        count+=1
    if count%2==0:
        return 0
    else:
        return 1

#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        # if it's empty, assign the head
        if self.head == None:
            self.head = node(val)
        # go through the linked list and put val at the end
        else:
            new_node = node(val)
            temp = self.head
            # terminates when temp.next == None
            while(temp.next):
                temp=temp.next
            # this temp.next currently == None, so we assign the new node value to it
            temp.next = new_node

# makes a n length linkedlist
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        if(isLengthEvenOrOdd(head)):
            print('Odd')
        else:
            print('Even')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends

# https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1#
