payment_number = 1
total_paid = 0
# blance, annualInterestRate, monthlyPaymentRate

while payment_number < 13:
    print "Month: " + str(payment_number)
    month_payment = round(monthlyPaymentRate * balance, 2)
    print 'Minimum monthly payment: ' + str(month_payment)
    total_paid += monthlyPaymentRate * balance
    balance = balance + (annualInterestRate/12.0) * balance
    balance = balance - (monthlyPaymentRate * balance)
    print('Remaining balance: ' + str(round(balance, 2)))
    payment_number += 1

print('Total paid: ' + str(round(total_paid, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
