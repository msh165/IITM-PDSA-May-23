def binary_search(l, v, count=1):
    print(l)
    left=0
    right=len(l)-1
    if l == []:
        return (False, count-1)
    mid = (left+right// 2)

    if v == l[mid]:
        return (True, count)
    elif v < l[mid]:
        return binary_search(l[:mid], v, count + 1)
    else:
        return binary_search(l[mid + 1:], v, count + 1)
