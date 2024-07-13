#Functions containing the code for the sorting algorithms
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def selectionsort(array):
    n = len(arr)
    for ind in range(n):
        min_index = ind
 
        for j in range(ind + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
#Asking user to choose which algorithm to use
#and to input an array of numbers to sort
arr = []
numofele = int(input("Enter the number of elements in the array: "))
if numofele > 1:
    for i in range(numofele):
        ele = int(input("Enter the element: "))
        arr.append(ele)
    num = int(input("Choose a sorting algorithm to use,\nBubble sort: 1\nSelection sort: 2\nInsertion sort: 3\n"))
    if num == 1:
        print("Chose 1")
        bubblesort(arr)
        print("The sorted array using bubble sort is: ")
        print(arr)
    elif num == 2:
        print("Chose 2")
        selectionsort(arr)
        print("The sorted array using selection sort is:")
        print(arr)
    elif num == 3:
        print("Chose 3")
        insertionsort(arr)
        print("The sorted array using insertion sort is: ")
        print(arr)
    else:
        print("Invalid value")
else:
    print("Array is already sorted")        
input("Press enter to exit.......")