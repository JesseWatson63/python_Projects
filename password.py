# Password
# Demonstrates the if statement

print("Welcome to the System Security Inc.")
print("-- where security is our middle name\n")

password = raw_input("Enter your password: ")

if password == "secret":
    print"Access Granted"

if password != "secret":
    print"Get out of here hacker"

input("\n\nPress the enter key to exit.")
