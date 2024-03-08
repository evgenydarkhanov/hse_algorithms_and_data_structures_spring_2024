import re


class PhoneNumbersRadixSort:
    def __init__(self, data_):
        self.data = data_
        self.result = None

    def _number_to_int(self, phone_number):
        result = re.sub(r"\D", "", phone_number)
        return int(result)

    def _data_preprocessing(self, data_):
        out = []
        for line in data_:
            elem = line.split()
            out.append((elem[0], "\t" + elem[1], self._number_to_int(elem[0])))
        return out

    def _one_digit_counting_sort(self, arr, exp):
        len_arr = len(arr)
        base = 10

        tmp = [0 for _ in range(base)]
        out = [0 for _ in range(len_arr)]

        for elem in arr:
            index = (elem[2] // exp) % base
            tmp[index] += 1

        for i in range(1, base):
            tmp[i] += tmp[i - 1]

        for i in range(len_arr - 1, -1, -1):
            index = (arr[i][2] // exp) % base
            out[tmp[index] - 1] = arr[i]
            tmp[index] -= 1

        for i in range(len_arr):
            arr[i] = out[i]

        return arr

    def _one_digit_radix_sort(self, arr):
        tmp = [elem[2] for elem in arr]
        max_value = max(tmp)
        exp = 1
        while max_value / exp >= 1:
            self._one_digit_counting_sort(arr, exp)
            exp *= 10

        return arr

    def sort(self):
        preprocessed_data = self._data_preprocessing(self.data)
        sorted_data_ = self._one_digit_radix_sort(preprocessed_data)
        result_list = [str(elem[0]) + elem[1] for elem in sorted_data_]
        self.result = [s + "\n" if s != result_list[-1] else s for s in result_list]
        return self.result

    def to_txt(self, filename):
        with open(filename, "w") as f:
            f.write(''.join(self.result))


data = []
with open("test_input_one.txt", "r") as file:
    for line in file:
        data.append(line)


solver = PhoneNumbersRadixSort(data)
sorted_data = solver.sort()
print(sorted_data)

output = []
with open("test_output_one.txt", "r") as file:
    for line in file:
        output.append(line)

print(output)
