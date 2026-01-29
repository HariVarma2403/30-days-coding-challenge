import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase)
    ]

    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak 😬"
    elif score == 3 or score == 4:
        return "Medium 💪"
    else:
        return "Strong 🔥"


def main():
    print("=== SMART PASSWORD GENERATOR ===")

    try:
        length = int(input("Enter password length: "))
        if length < 4:
            print("Length should be at least 4.")
            return
    except:
        print("Invalid number.")
        return

    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_numbers, use_symbols)
    strength = check_strength(password)

    print("\nGenerated Password:", password)
    print("Password Strength:", strength)


if __name__ == "__main__":
    main()
