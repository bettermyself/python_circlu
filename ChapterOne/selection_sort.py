def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in  range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

print(selectionSort([3,2,5,4,7]))
