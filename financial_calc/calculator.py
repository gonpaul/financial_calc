def calculate_simple_interest(principal, rate, time) -> float:
    if (principal < 0 or rate < 0 or time < 0):
        raise ValueError("Аргументы должны быть неотрицательными")

    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n=1):
    if not(n % 1 == 0 and n > 0 and rate >= 0 and time >= 0):
        raise ValueError(f'Некорректные аргументы: n = {n}, rate = {rate}, time = {time}')
    res = principal * (1 + rate/(100*n))**(n*time)
    return round(res, 2)

def calculate_tax(amount, tax_rate):
    if not(tax_rate >= 0 and tax_rate <= 100):
        raise ValueError(f'tax_rate должен быть в интервале [0, 100], tax_rate = {tax_rate}')
    return amount * tax_rate / 100

assert calculate_simple_interest(100, 10, 2) == 20