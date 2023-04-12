def Merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result


def MergeSort(array):
    if len(array) == 1:
        return array
    middle = len(array)//2
    left = MergeSort(array[:middle])
    right = MergeSort(array[middle:])
    return Merge(left, right)


array = [int(i)
         for i in input("Введіть елементи масиву через пробіл:").split()]
print(*array)
result = MergeSort(array)
print(*result)
