def binary_search(arr , target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high ) // 2
        print(f"Low = {low}, High = {high}, Mid = {mid} , Mid_value= {arr[mid]}")

        if arr[mid] == target:
            print (f"Successful search! Found at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
            print(f"{arr[mid]} < {target} -> Low = Mid + 1 = {low}\n")

        else:
            high = mid - 1
            print(f"{target} < {arr[mid]} -> High = Mid - 1 = {high}\n")

    return -1         # if target does not found


#Example :

numbers = [6, 12, 17, 38, 45, 55, 77, 84]

binary_search(numbers, 45)
