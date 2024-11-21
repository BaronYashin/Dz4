numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num == 1:
        continue
    is_prime = True
    for num1 in range(2, int(num/2)+1):
        if num % num1 == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print("Простые числа",primes)
print("Не простые числа", not_primes)