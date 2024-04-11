import solution
import unittest


class SolutionTestCase(unittest.TestCase):
    def test_original_data(self):       # исходные данные
        test_data = []
        solution.data_reading(test_data, './data/original_data.txt')
        
        expected = sorted(test_data, key=lambda x: x[0])
        solution.quick_sort_and_partition(test_data, key=lambda x: x[0])

        self.assertEqual(test_data, expected)
        
        
    def test_random_order(self):       # данные побольше в рандомном порядке
        test_data = []
        solution.data_reading(test_data, './test_data/test_random_order.txt')

        expected = sorted(test_data, key=lambda x: x[0])
        solution.quick_sort_and_partition(test_data, key=lambda x: x[0])

        self.assertEqual(test_data, expected)
        
        
    def test_reverse_order(self):       # данные побольше в обратном порядке
        test_data = []
        solution.data_reading(test_data, './test_data/test_reverse_order.txt')
        
        expected = sorted(test_data, key=lambda x: x[0])
        solution.quick_sort_and_partition(test_data, key=lambda x: x[0])

        self.assertEqual(test_data, expected)
        
          
    def test_single_element(self):       # массив из одного элемента
        test_data = []
        solution.data_reading(test_data, './test_data/test_single_element.txt')

        expected = sorted(test_data, key=lambda x: x[0])
        solution.quick_sort_and_partition(test_data, key=lambda x: x[0])

        self.assertEqual(test_data, expected)
        
    
    def test_stability(self):			# устойчивость
    	test_data = []
    	solution.data_reading(test_data, './test_data/test_stability.txt')
    	
    	expected = sorted(test_data, key=lambda x: x[0])
    	solution.quick_sort_and_partition(test_data, key=lambda x: x[0])
    	
    	if test_data == expected:
    		print('stable')
    	else:
    		print('unstable')
    	    	
    	self.assertIsNot(test_data, expected)

