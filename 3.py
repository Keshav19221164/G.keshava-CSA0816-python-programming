def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_and_composites(numbers):
    prime_count = 0
    composite_count = 0

    for num in numbers:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1

    return prime_count, composite_count

# Get user input
input_numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Count primes and composites
prime_count, composite_count = count_primes_and_composites(input_numbers)

print(f"Prime numbers count: {prime_count}")
print(f"Composite numbers count: {composite_count}")
