l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def traverse(id, arr):
    le = len(arr)

    for i in range(le):
        indx = (id + i) - 1
        if indx > len(arr) - 1:
            indx -= len(arr)
        print(arr[indx])
    return ''


print(traverse(6, l))