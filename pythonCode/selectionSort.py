#Find the smallest element in an odd array
def smallestFind(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in arr:
        if i <=smallest:
            smallest_index = arr.index(i)
    return smallest_index

#Sort Function
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        chosenIndex = smallestFind(arr)
        newArr.append(arr.pop(chosenIndex))
    return newArr

# main function
print selectionSort([1, 9, 4, 13, 25, 17, 10])