list_test = (5, 4, 3, 88, 2, 1)
ciag1 = ()
ciag2 = (1, 2, 5, 3, 1, 7, 9, 1, 12, 83, 1, 5, 3, 2)
ciag3 = (1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1)
ciag4 = (2, 2, 2, 2)
ciag5 = (1, 2)
ciag6 = (2, 1)

def bubble_sort(numbers):
    numbers = list(numbers)
    length = len(numbers)
    for i in range(length - 1):
        for item in range(length - 1 - i):
            if numbers[item] > numbers[item + 1]:
                temp = numbers[item + 1]
                numbers[item + 1] = numbers[item]
                numbers[item] = temp
    return numbers


print(bubble_sort(list_test))
print(bubble_sort(ciag1))
print(bubble_sort(ciag2))
print(bubble_sort(ciag3))
print(bubble_sort(ciag4))
print(bubble_sort(ciag5))
print(bubble_sort(ciag6))
