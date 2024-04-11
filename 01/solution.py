def partition(arr, low, high, key):
    pivot = key(arr[high])
    i = low - 1
    for j in range(low, high):
        if key(arr[j]) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high, key):
    if low < high:
        q = partition(arr, low, high, key)
        quick_sort(arr, low, q-1, key)
        quick_sort(arr, q+1, high, key)


def quick_sort_and_partition(arr, key):
    high = len(arr) - 1
    low = 0
    quick_sort(arr, low, high, key)
    

def convert_to_tuple(line):
    tmp = line.split()
    return (int(tmp[0]), tmp[1])


def data_reading(lst, filename):
    with open(filename, 'r') as file:
        for line in file:
            lst.append(convert_to_tuple(line))
            

test_original_data = []
data_reading(test_original_data, './data/original_data.txt')

print('original data')
for elem in test_original_data:
	print(*elem)
print()

quick_sort_and_partition(test_original_data, key=lambda x: x[0])
print('sorted data')
for elem in test_original_data:
	print(*elem)
print()
