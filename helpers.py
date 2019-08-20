alphabet_letters = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(letter):
    if letter in alphabet_letters:
        index = alphabet_letters.index(letter)
    else:
        letter = letter.lower()
        index = alphabet_letters.index(letter)
    return index


def rotate_character(char, rot):
    while not char.isalpha():
        return char
    rotated_index = alphabet_position(char) + rot
    if rotated_index < 26:
        new_string = alphabet_letters[rotated_index]
    else:
        new_string = alphabet_letters[rotated_index % 26]
    if char == char.upper():
        new_string = new_string.upper()
    return new_string
