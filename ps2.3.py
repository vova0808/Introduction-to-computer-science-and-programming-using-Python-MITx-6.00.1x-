balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
lower_bound = balance / 12
upper_bound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
epsilon = 0.01
remainBalance = balance
while remainBalance >= epsilon:
    payment = (upper_bound + lower_bound) / 2
    for month in range(1, 13):
        monthlyBalance = remainBalance - payment
        interest = monthlyInterestRate * monthlyBalance
        remainBalance = monthlyBalance + interest

    if remainBalance < 0:
        upper_bound = payment
        remainBalance = balance
    elif remainBalance > epsilon:
        lower_bound= payment
        remainBalance = balance
print("Lowest payment: ", round(payment, 2))                



