# Kevin Chen
# 10/24/17
# This program will encode or decode your text in Vigenere cipher


alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode_text():
    """
    This program represent the way to encode text
    :return:encode, the new text after encode
    """

    code_text = input("please enter the text you want to encode")

    code_text = code_text.lower()

    code_text = code_text.replace(' ', '')

    key = input("please enter the key")
    encode = ""
    for x in range(len(code_text)):
        num1 = alphabet.index(code_text[x])
        num2 = alphabet.index(key[x % len(key)])

        num = (num1+num2) % 26
        encode += alphabet[num]
    return(encode)


def decode_text():
    """
    This program represent the way to decode text
    :return: the text after decode
    """

    code = input("please enter the text you want to decode")

    code = code.lower()

    code = code.replace(' ', '')

    key = input("please enter the key")

    decode = ""
    for x in range(len(code)):
        num1 = alphabet.index(code[x])
        num2 = alphabet.index(key[x % len(key)])
        num = (num1-num2) % 26
        decode += alphabet[num]
    

    return(decode)


def main():
    choice = input("press e to encode, d to decode or q to quit")

    if choice in ["e", "E"]:
        print(encode_text())
    elif choice in ["d", "D"]:
        print(decode_text())
    elif choice in ["q", "Q"]:
        print("thanks for playing, have a great day")
main()
