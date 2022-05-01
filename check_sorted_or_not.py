def checksortedornot(arr):
    if len(arr) == 1:
        return True

    if arr[0] <= arr[1]:
        return checksortedornot(arr[1:])
    else:
        return False


arr = [1, 2, 3, 5, 7, 9]
arr1 = [1, 3, 4, 2, 11]
print(checksortedornot(arr))
print(checksortedornot(arr1))