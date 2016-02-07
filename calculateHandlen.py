def calculateHandlen(hand):
    hand_count = 0
    for letter in hand:
        if hand[letter] != 0:
            hand_count += hand[letter]
    return hand_count
print calculateHandlen({'a': 3, 'c': 0, 'b': 1})