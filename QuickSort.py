lst = ['T','E','L','E','P','A','T','H','Y']
def quickSort(List):
    if len(List) <= 1:
        return List
    lower = []
    higher = []
    pivot = List[0]
    for x in List[1:]:
        if x < pivot:
            lower.append(x)
        else:
            higher.append(x)
    return quickSort(lower)+[pivot]+quickSort(higher)

print(quickSort(lst))