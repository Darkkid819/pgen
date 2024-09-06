import random
import string
import argparse

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected (uppercase, lowercase, numbers, or special).")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    
    parser.add_argument('--length', type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument('--no-uppercase', action='store_false', help="Exclude uppercase letters")
    parser.add_argument('--no-lowercase', action='store_false', help="Exclude lowercase letters")
    parser.add_argument('--no-numbers', action='store_false', help="Exclude numbers")
    parser.add_argument('--no-special', action='store_false', help="Exclude special characters")

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_uppercase=args.no_uppercase,
        use_lowercase=args.no_lowercase,
        use_numbers=args.no_numbers,
        use_special=args.no_special
    )

    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

