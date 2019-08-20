from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted


def main():
    user_input = input("What is the message you want to encrypt? ")
    rot_number = int(input("What is the rotating number? "))

    print(encrypt(user_input, rot_number))


if __name__ == '__main__':
    main()
