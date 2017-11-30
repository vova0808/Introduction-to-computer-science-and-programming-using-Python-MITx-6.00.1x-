balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0

while month < 12:
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - monthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    month += 1
    
print("Remaining balance: " + str(round(balance, 2)))    
    
    
 