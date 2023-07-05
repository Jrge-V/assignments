import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--direction", dest="direction", choices=["encode", "decode"], help="Pick whether to encode or decode a word.")
parser.add_argument("--text", dest="text", type=str, help="Type your message.")
parser.add_argument("--shift", dest="shift", type=int, help="Type the shift number.")
args = parser.parse_args()


if args.direction is None:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    args.direction = direction.lower()

if args.text is None:
    text = input("Type your message:\n")
    args.text = text.lower()

if args.shift is None:
    shift = int(input("Type the shift number:\n"))



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    text = list(text)
    for i in range(len(text)):
        ind = alphabet.index(text[i]) + shift
        if ind >= len(alphabet):
            ind -= len(alphabet)

        text[i] = alphabet[ind]
    text = ''.join(text)

    print(f"The encoded text is {text}")

def decode(text, shift):
    text = list(text)
    for i in range(len(text)):
        ind = alphabet.index(text[i]) - shift
        text[i] = alphabet[ind]
    text = ''.join(text)

    print(f"The decoded text is {text}")


if args.direction == 'encode':
    encrypt(text, shift)

elif args.direction == 'decode':
    decode(text, shift)
else:
    print("Please specify encode or decode.")
