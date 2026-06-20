def isalpha(ch):
    return (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')


def encrypt(text, shift):
    result = ""
    for ch in text:                      
        if isalpha(ch):
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch                  
    return result


def decrypt(text, shift):
    result = ""
    for ch in text:
        if isalpha(ch):
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - start - shift) % 26 + start)
        else:
            result += ch
    return result


def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted text:", encrypt(text, shift))
            print()
        elif choice == 2:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted text:", decrypt(text, shift))
            print()
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
