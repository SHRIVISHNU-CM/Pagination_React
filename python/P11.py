#rotate array left side
def leftRotateByOne(arr):
    first = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]

    arr[-1] = first


def leftRotate(arr,r):
    if r<0 or r>=len(arr):
        return
    for i in range(r):
        leftRotateByOne(arr)


if __name__ == '__main__':
    arr = [ 1,2,3,4,5]
    r= 2

    res = leftRotate(arr,r)

    print(arr)