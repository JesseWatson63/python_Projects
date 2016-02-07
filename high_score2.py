# high Scores 2
# Demonstrates nested sequences

scores = []

choice = None
while choice != "0":

    print(
        """High Scores 2

           0 - Quit
           1 - List
           2 - Add High Score

        """)

    choice = raw_input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    elif choice == "2":
        name = raw_input("What is the player's name?: ")
        score = int(raw_input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # keep only top 5 scores
    else:
        print("Sorry, but", choice, "isn't a valid choice.")
