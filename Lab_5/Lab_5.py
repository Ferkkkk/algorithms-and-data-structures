class Sort():
    def Merge(self, Array, start, middle, end):
        if start <= middle and middle < end:
            n1 = middle - start + 1
            n2 = end - middle
            Left = [0] * (n1 + 1)
            Right = [0] * (n2 + 1)
            for i in range(n1):
                Left[i] = Array[start+i]
            for j in range(n2):
                Right[j] = Array[middle+j+1]
            Left[n1] = float('inf')
            Right[n2] = float('inf')
            i = j = 0
            for k in range(start, end+1):
                if Left[i] <= Right[j]:
                    Array[k] = Left[i]
                    i += 1
                else:
                    Array[k] = Right[j]
                    j += 1

    def MergeSort(self, Array, start, end):
        if start < end:
            middle = (start + end) // 2
            self.MergeSort(Array, start, middle)
            self.MergeSort(Array, middle+1, end)
            self.Merge(Array, start, middle, end)
        return Array

sort = Sort()
array = input('Введіть елементи масиву через пробіл: ').split()
array = [int(x) for x in array]
print(array)
result = sort.MergeSort(array, 0, len(array)-1)
print(result)