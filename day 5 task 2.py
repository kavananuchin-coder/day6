def power(base, exp):
    return base ** exp

def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)

# Main execution
result_power = power(2, 10)
numbers = [10, 20, 30, 40]
result_average = average(numbers)

print("2^10 =", result_power)
print("Average =", result_average)
