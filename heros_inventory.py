# Heros's Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ()

# Treat the tubple as a condition
if not inventory:
    print("You are empty-handed.")

raw_input("\nPress the enter key to continue.")

# Create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# Print each elemtent in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

raw_input("\n\nPress the enter button to exit.")