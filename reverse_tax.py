#reverse_tax
#to reverse calculate pre tax price

def reverse_tax(tp,tax_percent):
	pre_tax_price  = tp / ((tax_percent /100) + 1 )
	print('\n Pre Tax Amount, for TAX% {x} is: {y}'.format(x = float(tax_percent), y = float(pre_tax_price)))

while True:
	print('\n ReverZ Tax Calculator v1.0')
	tp = float(input(' \n Enter Tax inclusive Amout: '))
	tax_percent = float(input(' \n Enter tax percentage: '))
	reverse_tax(tp, tax_percent)

