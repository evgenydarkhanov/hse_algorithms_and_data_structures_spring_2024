import random
import string


def generate_data(lines, length, order=['random', 'reverse', None], max_value=100):
    random_lines = []
    numbers = list(range(lines))
    if order == 'random':
        random.shuffle(numbers)
    if order == 'reverse':
        numbers = numbers[::-1]
    if order is None:
        numbers = [random.randint(0, max_value) for _ in range(lines)]

    for i in range(lines):
        number = str(numbers[i])
        letters = string.ascii_letters 
        rand_string = ''.join(random.choice(letters) for i in range(length))
        elem = (number + '\t' + rand_string + '\n')
        random_lines.append(elem)
    
    random_lines[-1] = random_lines[-1].rstrip()
    return random_lines
    

def to_txt(filename, lst):
    with open(filename, 'w') as f:
        f.write(''.join(lst))
        
DIR_NAME = './test_data/'

data_for_tests = ['test_random_order',
                  'test_reverse_order',
                  'test_stability']

arguments = [[1000, 10, 'random'],
             [900, 10, 'reverse'],
             [1000, 10, None]]

for i in range(len(data_for_tests)):
    to_txt(DIR_NAME + data_for_tests[i] + '.txt', generate_data(*arguments[i]))

test_single_element = ['31\tdgiFATToGK']
to_txt(DIR_NAME + 'test_single_element.txt', test_single_element)

