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
    
    def CountingRadixSort(self, InputArray, digit):
        TempArray = [0] * (max(InputArray) + 1)
        OutputArray = [0] * len(InputArray)
        for j in range(len(InputArray)):
            TempArray[(InputArray[j] // (10**digit)) % 10] += 1
        for i in range(1, len(TempArray)):
            TempArray[i] += TempArray[i-1]
        for j in range(len(InputArray)-1, -1, -1):
            digit_value = (InputArray[j] // (10**digit)) % 10
            OutputArray[TempArray[digit_value]-1] = InputArray[j]
            TempArray[digit_value] -= 1
        for i in range(len(InputArray)):
            InputArray[i] = OutputArray[i]

    def RadixSort(self, InputArray):
        max_digit = len(str(abs(max(InputArray))))
        for i in range(max_digit):
            self.CountingRadixSort(InputArray, i)

        return InputArray


# main
sort = Sort()
array = [int(i)
         for i in input("Введіть елементи масивiу через пробіл:").split()]
print("Ваш масив:", *array)
if len(str(abs(max(array)))) >= 3:
    result = sort.RadixSort(array)
    print("Відсортований by RadixSort:", *result)
else:
    result = sort.CountingSort(array)
    print("Відсортований by CountingSort:", *result)