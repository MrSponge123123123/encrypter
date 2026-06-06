import math
from random import Random

dictionary: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    ".", ":", ",", ";", "-", "_", "#", "+", "*", "~", "<", ">", "|", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "{", "}", "[", "]", "´", "`", "\\", " "]


def encrypt(message: str) -> str:
    rand = Random()
    encrypted_message: str = ""

    for pos in range(len(message)):
        char: str = message[pos]
        reverse_value: bool = rand.choice([True, False])
        value: int = dictionary.index(char) if not reverse_value else int(math.fabs(dictionary.index(char) - len(dictionary)) - 1)

        formatted_value: str = f"{value:02}"
        encrypted_char: str = f"{formatted_value[0]}{rand.randint(0, 4) if not reverse_value else rand.randint(5, 9)}{formatted_value[1]}{pos}"

        encrypted_message += f"{encrypted_char} "

    return encrypted_message


