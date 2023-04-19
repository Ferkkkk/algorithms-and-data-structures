class Sort():
    def CountingSort(self, InputArray):
        TempArray = [0] * (max(InputArray) + 1)
        OutputArray = [0] * len(InputArray)
        for j in range(len(InputArray)):
            TempArray[InputArray[j]] += 1
        for i in range(1, len(TempArray)):
            TempArray[i] += TempArray[i-1]
        for j in range(len(InputArray)-1, -1, -1):
            OutputArray[TempArray[InputArray[j]]-1] = InputArray[j]
            TempArray[InputArray[j]] -= 1
        return OutputArray

    def RadixSort(self, Array):
        pass


# main
sort = Sort()
array = [int(i)
         for i in input("Введіть елементи масиву через пробіл:").split()]
print("Ваш масив:", *array)
result1 = sort.CountingSort(array)
print("Відсортований by CountingSort:", *result1)
#result2 = sort.RadixSort(array)
#print("Відсортований by RadixSort:", *result2)