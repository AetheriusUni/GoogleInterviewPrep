# Priority Queue implementation in Python
# max priority on top, so max heap


# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    # left node index is 2i+1
    l = 2 * i + 1
    # right node index is 2i+2
    r = 2 * i + 2
    # if the left node is located higher on the heap and the value of the current largest node is less than its left node
    if l < n and arr[i] < arr[l]:
        # make the largest node the left node instead
        largest = l
    # if the right node is located higher on the heap and the value of the current largest node is less than its right node
    if r < n and arr[largest] < arr[r]:
        # make the largest node the right node instead
        largest = r

    # recursively heapify until the tree is fixed    
    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    # if tree is empty, add node to tree
    if size == 0:
        array.append(newNum)
    # else add the node to the tree
    else:
        array.append(newNum)
        # then heapify upwards
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    # at this point 'i' is the index of num; swap the values of num and the last node in the tree
    array[i], array[size - 1] = array[size - 1], array[i]
    # remove the last node in the tree
    array.remove(size - 1)
    # after deletion make sure to fix the tree
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
