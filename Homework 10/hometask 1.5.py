import random
def generate_random_list_nums(n, start, end):
    return [random.randint(start, end) for _ in range(n)]
def count_identical_numbers(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts
def print_function(counts):
    for k, v in counts.items():
        print(f'Элемент {k} встречается {v} раз(а)')

n = 10
start = 1
end = 9

random_list = generate_random_list_nums(n, start, end)
print('Сгенерированный список:', random_list)

count_identical_numbers = count_identical_numbers(random_list)
print_function(count_identical_numbers)