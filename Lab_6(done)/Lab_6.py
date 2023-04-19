import random


class Sort():
    def QuickSort(self, Array):
        if len(Array) <= 1:
            return Array
        unit = self.Partition(Array)
        Left = self.QuickSort(Array[:unit])
        Right = self.QuickSort(Array[unit:])
        return Left + Right

    def RandomizedQuickSort(self, Array):
        if len(Array) <= 1:
            return Array
        unit = self.RandomizedPartition(Array)
        Left = self.RandomizedQuickSort(Array[:unit])
        Right = self.RandomizedQuickSort(Array[unit:])
        return Left + Right

    def Partition(self, Array):
        unit = Array[-1]
        i = -1
        for j in range(len(Array)-1):
            if Array[j] <= unit:
                i += 1
                Array[i], Array[j] = Array[j], Array[i]
        Array[i+1], Array[-1] = Array[-1], Array[i+1]
        return i+1

    def RandomizedPartition(self, Array):
        i = -1
        unit_index = random.randint(0, len(Array)-1)
        unit = Array[unit_index]
        for j in range(len(Array)-1):
            if Array[j] <= unit:
                i += 1
                Array[i], Array[j] = Array[j], Array[i]
        Array[i+1], Array[unit_index] = Array[unit_index], Array[i+1]
        return self.Partition(Array)


sort = Sort()
array = [int(i)
         for i in input("Введіть елементи масиву через пробіл:").split()]
print("Ваш масив:", *array)
result1 = sort.QuickSort(array)
print("Відсортований by QuickSort:", *result1)
result2 = sort.RandomizedQuickSort(array)
print("Відсортований by RandomizedQuickSort:", *result2)
