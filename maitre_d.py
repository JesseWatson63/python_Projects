# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening. \n")

money = int(raw_input("How many dollars do you slip the Maitre D'?"))

if money:
    print("Ah, Iam remindedof a table.  Right this way.")
else:
    print("Please, sit.  It may be a while.")

raw_input("\n\nPress the enter key to exit.")
