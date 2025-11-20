def bubble_sort(dataList):
    lst = dataList

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2) or (num1 < num2):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
arr = [10, 4, 7, 9, 25, 11, 3]
print("Unsorted:", arr)
print("Sorted:", bubble_sort(arr))