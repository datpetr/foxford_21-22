answer = []

for number in range(318216, 369454):
    prime_divisors, possible_divisor, current = [], 2, number
    while possible_divisor ** 3 <= current:
        if current % possible_divisor == 0:
            prime_divisors.append(possible_divisor)
            current //= possible_divisor
        else:
            possible_divisor += 1
    if current != 1:
        prime_divisors.append(current)

    if len(prime_divisors) == 3 and len(set(prime_divisors)) == 3:
        last_digit = prime_divisors[0] % 10

        if all(p % 10 == last_digit for p in prime_divisors):
            answer.append(number)


print(len(answer))
print(min(answer))
