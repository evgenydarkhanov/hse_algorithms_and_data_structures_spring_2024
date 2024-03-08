import unittest
import solution


def data_reading(lst, filename):
    with open(filename, 'r') as file:
        for line in file:
            lst.append(line)


class FirstTestCase(unittest.TestCase):
    def test_input_one(self):       # данные примера
        input_one = []
        data_reading(input_one, "test_input_one.txt")

        solver = solution.PhoneNumbersRadixSort(input_one)
        actual = solver.sort()

        expected = []
        data_reading(expected, "test_output_one.txt")

        self.assertEqual(actual, expected)

    def test_input_two(self):       # проверка на усточивость
        input_two = []
        data_reading(input_two, "test_input_two.txt")

        solver = solution.PhoneNumbersRadixSort(input_two)
        actual = solver.sort()

        expected = []
        data_reading(expected, "test_output_two.txt")

        self.assertNotEqual(actual, expected)

    def test_input_three(self):     # данные побольше
        input_three = []
        data_reading(input_three, "test_input_three.txt")

        solver = solution.PhoneNumbersRadixSort(input_three)
        actual = solver.sort()

        expected = []
        data_reading(expected, "test_output_three.txt")

        self.assertEqual(actual, expected)
