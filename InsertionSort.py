def insertion_sort (arr):

    for i in range ( 1 , len(arr)):
        key = arr [i]
        j = i - 1         # j is step before the i 

        while j >= 0 and arr[j] > key :
            arr [j + 1] = arr[j]
            j -=1
        arr [j+1 ] = key 
    return arr 


num = [ 12, 11, 13, 14 , 5]
print ("Original list:" , num)

sorted_numbers = insertion_sort(num)
print("Sorted list : ", sorted_numbers)
