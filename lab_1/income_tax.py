# tax_payer
name = input('Enter your name: ')

# to calculate the income tax

income = eval(input('Enter your income: '))
num_of_child = int(input('How many children do you have: '))

tax = 0.25 * (income * 11 - num_of_child * 450)

print()

print('Tax Payer!')
print(name)
if tax > 0:
	
	print(f'Tax amount: {tax}')
else:
	print(f'time time you dont need to pay tax, {tax}!!')