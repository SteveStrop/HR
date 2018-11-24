# l1 = [3, 5, 7, 9]
# l2 = [2, 4, 6, 8, 10]


def do_merge_sort(l1, l2):
    res = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    return res


def merge_sort(l):
    if len(l) <2:
        return l[:]
    else:
        mid = len(l)//2
        l1 = merge_sort(l[:mid])
        l2 = merge_sort(l[mid:])
        return do_merge_sort(l1,l2)
print(merge_sort([8,5,9]))
