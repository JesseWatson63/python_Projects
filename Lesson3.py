# Lesson 3 Functions and Modules
costs = [5, 10, 15, 20]


def sum_cart(items):
	total_cost = 0
	for x in costs:
		total_cost += x
	return total_cost

print sum_cart(costs)