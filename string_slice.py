# Pizza Slicer
# Demonstrates string slicing

word = "pizza"

print(
    """
    Slicing the 'cheat sheet'
    0   1   2   3   4   5
    +---+---+---+---+---+
    | P | I | Z | Z | A |
    +---+---+---+---+---+
    -5   -4   -3   -2   -1

    """)

print"Enter the beginning and ending index for your slice of 'pizza'."
print"Press the enter key at 'Start' to exit."
start = None
while start != "":
    start = (raw_input("\nStart: "))

    if start:
        start = int(start)

        finish = int(raw_input("Finish: "))

        print"word[", start, ":", finish, "] is"
        print(word[start:finish])

raw_input("\n\nPress the enter key to exit.")
