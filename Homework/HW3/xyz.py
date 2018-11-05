from random import randint
def find(a):
    a = qsort(a)

    result = []
    i = 0
    for z in a:
        left = 0
        right = i - 1
        while left < right:
            if (a[left] + a[right] == z):
                result.append([a[left], a[right] , z])
                left += 1
                right -= 1
            elif a[left] + a[right] < z:
                left += 1
            elif a[left] + a[right] > z:
                right -= 1
        i += 1
    return result


def qsort(a):
    if a == []:
        return []
    index = randint(0,len(a) - 1)
    a[0], a[index] = a[index], a[0]
    pivot = a[0]

    left = [x for x in a[1:] if x <= pivot]
    right = [x for x in a[:] if x > pivot]
 
    return qsort(left) + [pivot] + qsort(right)

print(find(list(range(0,10))))
