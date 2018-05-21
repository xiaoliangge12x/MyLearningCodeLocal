# quickSort Function, based on Recursion Methods
def quickSort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[0]
        lowerSubArr = [i for i in arr[1:] if i<=pivot]   #except the arr[0]
        higherSubArr = [i for i in arr[1:] if i>pivot]
        return quickSort(lowerSubArr)+[pivot]+quickSort(higherSubArr)

#Main Function
list = [1,4,3,9,13,7,20,6]
print quickSort(list)