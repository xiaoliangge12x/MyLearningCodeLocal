# BinarySearch Test
#import math
def Binary_Search(list, item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)/2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid +1
        else:
            high = mid-1
    return None

testList =[1,4,7,9,10,13,16]
print Binary_Search(testList, 10)    # Don't forget: The index number starts from zero
print Binary_Search(testList, 4)
print Binary_Search(testList, 6)