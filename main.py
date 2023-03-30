import csv
import json
import math
import random


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }
            with open(filename, 'a+', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=2, ensure_ascii=False)
                outfile.write('\n')
            return result

        return wrapper

    return decorator


def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number 1', 'Number 2', 'Number 3'])
        for i in range(num_rows):
            row = [random.randint(0, 1000) for _ in range(3)]
            writer.writerow(row)


def solve_quadratic_equation_with_csv(filename):
    def decorator(func):
        @save_to_json('results.json')
        def wrapper(*args, **kwargs):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # пропускаем заголовок
                for row in reader:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f'{row}: {result}')

        return wrapper

    return decorator


@solve_quadratic_equation_with_csv('data.csv')
def solve_quadratic_equation(a, b, c):
    pass


generate_csv_file('data.csv', 5)
solve_quadratic_equation(1, -5, a=12)
