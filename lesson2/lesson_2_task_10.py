def bank(X, Y):
    amount = X
    interest_rate = 0.10
    
    for _ in range(Y):
        amount += amount * interest_rate
    
    return amount

initial_deposit = 1000  # Например, 1000 рублей
years = 5  # Например, 5 лет

final_amount = bank(initial_deposit, years)
print("Сумма на счету спустя", years, "лет:", final_amount)