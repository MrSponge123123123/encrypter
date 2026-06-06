import math
from random import Random

dictionary: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    ".", ":", ",", ";", "-", "_", "#", "+", "*", "~", "<", ">", "|", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "{", "}", "[", "]", "´", "`", "\\", " "]


def encrypt(message: str) -> str:
    rand = Random()
    encrypted_chars: list[str] = []

    for pos in range(len(message)):
        char: str = message[pos]
        reverse_value: bool = rand.choice([True, False])
        value: int = dictionary.index(char) if not reverse_value else int(math.fabs(dictionary.index(char) - len(dictionary)) - 1)

        formatted_value: str = f"{value:02}"
        encrypted_char: str = f"{formatted_value[0]}{rand.randint(0, 4) if not reverse_value else rand.randint(5, 9)}{formatted_value[1]}{pos}"

        encrypted_chars.append(encrypted_char)

    randomised_encrypted_chars: list[str] = []
    while len(encrypted_chars) > 0:
        index: int = rand.randint(0, len(encrypted_chars) - 1)
        randomised_encrypted_chars.append(encrypted_chars[index])
        encrypted_chars.pop(index)

    encrypted_message: str = ""
    for encrypted_char in randomised_encrypted_chars:
        encrypted_message += f"{encrypted_char} "

    return encrypted_message


def decrypt(encrypted_message: str) -> str:
    while encrypted_message[-1] == " ":
        encrypted_message = encrypted_message.removesuffix(" ")

    encrypted_chars: list[str] = encrypted_message.split(" ")

    decrypted_chars: dict[int, str] = {}

    for encrypted_char in encrypted_chars:
        value: int = int(f"{encrypted_char[0]}{encrypted_char[2]}") if int(encrypted_char[1]) < 5 \
            else -int(math.fabs(int(f"{encrypted_char[0]}{encrypted_char[2]}") + 1)) + len(dictionary)

        char: str = dictionary[value]
        pos: int = int(encrypted_char[3:])

        decrypted_chars[pos] = char

    decrypted_message: str = ""
    for index in range(len(decrypted_chars)):
        decrypted_message += decrypted_chars[index]

    return decrypted_message