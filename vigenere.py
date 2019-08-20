from helpers import alphabet_position, rotate_character


def encrypt(original_text, key):
    encrypted = []
    starting_index = 0
    for letter in original_text:
        rot = alphabet_position(key[starting_index])
        if not letter.isalpha():
            encrypted.append(letter)
            continue
        # print(letter, key[starting_index], rot)

        encrypted.append(rotate_character(letter, rot))
        if starting_index == (len(key) - 1):
            starting_index = 0
        else:
            starting_index += 1

    return ''.join(encrypted)


def main():
    user_input = input("What is the message you want to encrypt? ")
    key_word = input("What is the keyword you want to use today? ")

    print(encrypt(user_input, key_word))


if __name__ == '__main__':
    main()
