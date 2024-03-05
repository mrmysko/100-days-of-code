# Todo - Add salt.
# Todo - Add more complex encryption?


def main():

    while True:
        encode_decode = (
            input("Type 'encode' to encrypt, or 'decode' to decrypt: ").lower().strip()
        )
        if encode_decode == "encode" or encode_decode == "decode":
            break

    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    print(crypt(encode_decode, message, shift))


def crypt(type: str, message: str, shift: int):
    out_message = []

    if type == "encode":
        out_message = [chr(ord(x) + shift) for x in message]
    elif type == "decode":
        out_message = [chr(ord(x) - shift) for x in message]

    out_message = "".join(out_message)
    return out_message


if __name__ == "__main__":
    main()
