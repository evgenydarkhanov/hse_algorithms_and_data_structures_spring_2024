import random
import string

from solution import convert_to_tuple


def generate_data_random(lines, length):
    random_lines = []
    numbers = string.digits
    letters = '39ant'

    for i in range(lines):
        if i % 2 == 0:
            rand_number = '+7-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))
        else:
            rand_number = '+375-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))

        rand_string = ''.join(random.choice(letters) for i in range(length))
        elem = (rand_number + '\t' + rand_string + '\n')
        random_lines.append(elem)

    random.shuffle(random_lines)
    random_lines[-1] = random_lines[-1].rstrip()
    return random_lines
    

def generate_data_reverse(lines, length):
    random_lines = []
    numbers = string.digits
    letters = '39ant'

    for i in range(lines):
        if i % 2 == 0:
            rand_number = '+7-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))
        else:
            rand_number = '+375-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))

        rand_string = ''.join(random.choice(letters) for i in range(length))
        elem = (rand_number + '\t' + rand_string + '\n')

        random_lines.append(convert_to_tuple(elem))

    random_lines.sort(key = lambda x: -x[2])
    random_lines = [elem[0] + '\t' + elem[1] + '\n' for elem in random_lines]

    random_lines[-1] = random_lines[-1].rstrip()
    return random_lines
    
    
def generate_data_stability(lines, length):
    random_lines = []
    numbers = string.digits
    letters = '39ant'

    rand_numbers = []
    for i in range(lines // 10):
        if i % 2 == 0:
            rand_number = '+7-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))
        else:
            rand_number = '+375-' + ''.join(random.choice(numbers) for i in range(3)) + '-' + ''.join(random.choice(numbers) for i in range(7))
        rand_numbers.append(rand_number)

    rand_numbers *= 10

    for i in range(lines):
        rand_string = ''.join(random.choice(letters) for i in range(length))
        elem = (rand_numbers[i] + '\t' + rand_string + '\n')
        random_lines.append(elem)

    random.shuffle(random_lines)
    random_lines[-1] = random_lines[-1].rstrip()
    return random_lines
    

def to_txt(filename, lst):
    with open(filename, 'w') as f:
        f.write(''.join(lst))
        

DIR = './test_data/'        
        
        
test_random_order = generate_data_random(1000, 64)
to_txt(DIR + 'test_random_order.txt', test_random_order)

test_reverse_order = generate_data_reverse(1000, 64)
to_txt(DIR + 'test_reverse_order.txt', test_reverse_order)

test_stability = generate_data_stability(1000, 64)
to_txt(DIR + 'test_stability.txt', test_stability)

test_single_element = ['+7-495-1123212\tn399tann9nnt3ttnaaan9nann93na9t3a3t9999na3aan9antt3tn93aat3naa']
to_txt(DIR + 'test_single_element.txt', test_single_element)

