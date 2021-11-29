my_numbers = list(map(int,input("Введите целые числа через пробел \n").split()))

def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


random_number = int(input("Введите число: "))

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

def control_numbers(a):
    count = 0
    for b in a:
        if b != random_number:
            count += 1
    if count == len(a):
        print("Число которое Вы ввели отсутствует в последовательности")
    else:
        pass
control_numbers(my_numbers)


number_list = [int(s) for s in my_numbers]
sorted_number_list = sort(number_list)
print(sorted_number_list)
print("id = ", binary_search(sorted_number_list, random_number, 0, len(sorted_number_list) - 1))