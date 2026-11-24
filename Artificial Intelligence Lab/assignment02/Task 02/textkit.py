
def rle_encode(text):
    if text == "":
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

    return result


def rle_decode(code):
    result = ""
    i = 0

    while i < len(code):
        char = code[i]
        i += 1

        count = ""

        while i < len(code) and code[i].isdigit():
            count += code[i]
            i += 1

        if count == "":
            raise ValueError("Invalid encoded string")

        result += char * int(count)

    return result


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


if __name__ == "__main__":
    print(rle_encode("aaabbc"))
    print(rle_decode("a3b2c1"))
    print(caesar_encrypt("hello", 3))
    print(caesar_decrypt("khoor", 3))
    print(is_palindrome("madam"))
