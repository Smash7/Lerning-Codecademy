# 15.
def vpadlu():
    pass


# 3.
def score_word(word: str) -> int:
    # 4.
    point_total = 0
    # 5.
    for i in word:
        if i in list(letter_to_points):
            point_total += letter_to_points[i]
    # 6.
    return point_total


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# 1.
letter_to_points = {key: value for key, value in zip(letters, points)}

# 2.
letter_to_points[" "] = 0

# 7.
brownie_points = score_word("BROWNIE")

# 8.
print(brownie_points)

# 9.
player_to_words = {"BLUE": ["EARTH", "ERASER", "ZAP"],
                   "TENNIS": ["EYES", "BELLY", "COMA"],
                   "EXIT": ["MACHINE", "HUSKY", "PERIOD"]}

# 10.
player_to_points = {}

# 11.
for player, words in player_to_words.items():
    player_points = 0

    # 12.
    for word in words:
        player_points = score_word(word)

    # 13.
    player_to_points[player] = player_points

# 14.
print(player_to_points)
