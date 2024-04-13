import re

# препроцессинг номеров
def number_to_int(phone_number):
    result = int(re.sub(r'\D', '', phone_number))
    return result

# превращает в кортеж (телефон, str, int(телефон))
def convert_to_tuple(line):
    tmp = line.split()
    return (tmp[0], tmp[1], number_to_int(tmp[0]))

# читает данные из файла, преобразует к формату (телефон, str, int(телефон))
def data_reading(lst, filename):
    with open(filename, 'r') as file:
        for line in file:
            lst.append(convert_to_tuple(line))

# преобразует сортированные данные к исходному формату
def data_to_original_format(sorted_data):
    result_tmp = [elem[0] + '\t' + elem[1] for elem in sorted_data]
    result = [s + '\n' if s != result_tmp[-1] else s for s in result_tmp]
    return result
    
# удобнее было сделать классом
class PhoneNumbersRadixSort:
    def __init__(self, data, result=None):
        self.data = data
        self.result = result

    def counting_sort(self, arr, digit, base, key):
        length = len(arr)

        tmp = [0 for _ in range(base)]
        out = [0 for _ in range(length)]

        for elem in arr:
            index = (key(elem) // digit) % base
            tmp[index] += 1

        for i in range(1, base):
            tmp[i] += tmp[i-1]

        for elem in arr[::-1]:
            index = (key(elem) // digit) % base
            out[tmp[index] - 1] = elem
            tmp[index] -= 1

        for i in range(length):
            arr[i] = out[i]

        return arr

    def radix_sort(self, arr, key):
        base = 10
        digit = 1
        tmp = [key(elem) for elem in arr]
        max_value = max(tmp)
        while max_value / digit >= 1:
            self.counting_sort(arr, digit, base, key)
            digit *= 10

        return arr

    def sort(self, key):
        sorted_data = self.radix_sort(self.data, key=key)
        result_list = [elem[0].lstrip() + '\t' + elem[1] for elem in sorted_data]
        self.result = [s + '\n' if s != result_list[-1] else s for s in result_list]
        return self.result
        
