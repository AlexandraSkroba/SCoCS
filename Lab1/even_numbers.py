from random import sample


def rand_int_list():
    return sample(range(10), 5)


def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]
