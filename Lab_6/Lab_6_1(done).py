class Sort():
    def QuickSort(self, A):
        if len(A) <= 1:
            return A
        unit = self.Partition(A)
        Left = self.QuickSort(A[:unit])
        Right = self.QuickSort(A[unit:])
        return Left + Right

    def Partition(self, A):
        unit = A[-1]
        i = -1
        for j in range(len(A)-1):
            if A[j] <= unit:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[-1] = A[-1], A[i+1]
        return i+1

    def RandomizedPartition(self,):
        pass


sort = Sort()
array = [int(i)
         for i in input("Введіть елементи масиву через пробіл:").split()]
print(*array)
result = sort.QuickSort(array)
print(*result)
