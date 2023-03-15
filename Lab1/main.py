from hello_world import print_hello_world
from calculate import calculate
from even_numbers import rand_int_list
from even_numbers import get_even_numbers

if __name__ == '__main__':
    print_hello_world()
    print(calculate(1, 9, 'add'))

    numbers = rand_int_list()
    print(get_even_numbers(numbers))
