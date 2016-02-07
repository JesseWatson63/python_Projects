# High Scores
# Demonstrates list methods

scores = []
choice = None

while choice != "0":
    print(
        """
        High Scores
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score
        4 - Sort Scores
        """)
    choice = raw_input("Choice: ")

# Exit
    if choice == "0":
        print"Good-Bye."
# List high-Score table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(scores)
# Add a score
    elif choice == "2":
        score = int(raw_input("What score did you get?"))
        scores.append(score)
# Remove a score
    elif choice == "3":
        score = int(raw_input("Remove whch score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")
# Sort scores
    elif choice == "4":
        scores.sort(reverse=True)
# Some unknown choice
    else:
        print("sorry, but", choice, "isn't a valid choice.")

raw_input("\n\nPress the enter button to exit")
