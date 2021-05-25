lst = ['T','E','L','E','P','A','T','H','Y']
start = 0
end = len(lst)-1


def quickSort(lst, start, end):
    if start >= end:
        return 
    pivot = lst[end]
    left, right = start, end-1
    while left <= right:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and lst[right] >= pivot:
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
    lst[left], lst[end] = lst[end], lst[left] 
    quickSort(lst, start, left-1)
    quickSort(lst, left+1, end)
    return lst
print(quickSort(lst, start, end))