import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, custom_word=""):
    # Define character pools based on user choices
    upper_chars = string.ascii_uppercase if use_upper else ''
    lower_chars = string.ascii_lowercase if use_lower else ''
    digit_chars = string.digits if use_digits else ''
    symbol_chars = string.punctuation if use_symbols else ''
    
    all_chars = upper_chars + lower_chars + digit_chars + symbol_chars
    
    if not all_chars:
        return "Error: At least one character type must be selected!"

    # Ensure password has enough space for the custom word
    password_length = max(length, len(custom_word))
    
    # Generate the random part of the password
    random_part = ''.join(random.choice(all_chars) for _ in range(password_length - len(custom_word)))

    # Shuffle to mix the custom word with the random characters
    final_password = list(custom_word + random_part)
    random.shuffle(final_password)
    
    return ''.join(final_password)

# User Input
length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
custom_word = input("Enter a word/number to include (or press Enter to skip): ")

# Generate and display password
password = generate_password(length, use_upper, use_lower, use_digits, use_symbols, custom_word)
print(f"\nGenerated Password: {password}")
