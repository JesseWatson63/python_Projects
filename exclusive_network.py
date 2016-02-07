# Exclusive network
# Demonstrates logical operators and compond conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = raw_input("Username: ")

password = ""
while not password:
    password = raw_input("Password: ")

if username == "J.Watson" and password == "secret":
    print("Hi, Jesse.")
    security = 5
elif username == "S.meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Whats up, shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
elif username == "guest" or password == "guest":
    print("Welcome, guest.")
    security = 1
else:
    print("Login Failed. You're not so exclusive. \n")

raw_input("\n\nPress the enter key to exit")
