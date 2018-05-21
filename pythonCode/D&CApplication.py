# Divide and conquer alogrithm realization
# example: calculate the array's sum
def sumOfArray(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+sumOfArray(arr[1:])

def numberOfElements(list):
    if list == []:
        return 0
    list.pop(0)
    return 1+numberOfElements(list)

def maxElementInList(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return  list[0]
    else:
        if list[0]<=list[1]:
            list.pop(0)
            return maxElementInList(list)
        else:
            list.pop(1)
            return maxElementInList(list)

#main function
#print sumOfArray([1,2,3])
#print numberOfElements([1,2,3,4,4912389,7])
#print numberOfElements([])
print maxElementInList([1,4,3,7,5])
#list = [1,4,3,7,5]
#print list[0,2:]
#print list
#print list[0]