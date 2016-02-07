# Finicky Counter
# Demonstrates the break and continue statements

count = 0
while True:
    count += 1
    # end loog if count greater than 10
    if count > 10:
        break
    # Skip 5
    if count == 5:
        continue
    print(count)

raw_input("\n\n Press the enter key to exit")
