lst = ['T','E','L','E','P','A','T','H','Y']
def insertion_sort(lst):
    for i in range(1, len(lst)):
        min, j = lst[i], i - 1
        while j >= 0 and min < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j+1] = min
        print(lst)

insertion_sort(lst)