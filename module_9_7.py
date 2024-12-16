def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        a = 0
        for i in range(2, result+1):
            if result % i == 0:
                a += 1
        if a != 0:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)