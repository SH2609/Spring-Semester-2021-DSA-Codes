lst = ['T','E','L','E','P','A','T','H','Y']

def bubbleSort(lst):
    n = len(lst)-1
    for i in range(n):
        for j in range(0, n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
bubbleSort(lst)

