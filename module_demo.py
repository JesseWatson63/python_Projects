def add_tax(price, tax_rate):
	new_price = price / 100 * (100 * tax_rate)
	return new_price