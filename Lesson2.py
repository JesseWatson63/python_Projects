isAlive = True
a = 15
b = 24

myList = [1, 2, 3]

for a in myList:
	print a
	print a + 3
	print "start loop again."

while a < b:
	print a
	a += 1

for a in range(3):
	for b in range(4):
		print a * b