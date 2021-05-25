lst = lst = [9,7,4,2,3,1,8,1]
def mergeSort(List, column):
    max = len(List)
    if max > 1:
        mid = max//2

        Left = List[:mid]
        Right = List[mid:]

        mergeSort(Left, column)

        mergeSort(Right, column)

        R = L = 0

        while R < len(Right) and L < len(Left):
            if Right[R] < Left[L]:
                List[R+L] = Right[R]
                R += 1
            else:
                List[R+L] = Left[L]
                L += 1
        while R < len(Right):
            List[R+L] = Right[R]
            R += 1
        while L < len(Left):
            List[R+L] = Left[L]
            L += 1
    return (List)
print(mergeSort(lst, 0))
