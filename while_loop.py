num = 302

if num < 0:
    is_neg = True
    num = abs(num)
else:
    isNeg = False
result = ""
if num == 0:
    result = '0'
while num > 2:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result
    
print result