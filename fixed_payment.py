balance = 3926.00
annualInterestRate = .2


monthly_interest_rate = annualInterestRate / 12

for i in range(1, 7):
 
    updated_balance = balance + (balance * monthly_interest_rate)

    balance = round(updated_balance, -1)

    fixed_payment = balance / 12

print round(fixed_payment, -1)

