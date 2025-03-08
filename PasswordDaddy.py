import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, custom_word=""):
    upper_chars = string.ascii_uppercase if use_upper else ''
    lower_chars = string.ascii_lowercase if use_lower else ''
    digit_chars = string.digits if use_digits else ''
    symbol_chars = string.punctuation if use_symbols else ''
    
    all_chars = upper_chars + lower_chars + digit_chars + symbol_chars
    if not all_chars:
        return "Error: At least one character type must be selected!"
    
    required_chars = []
    if use_upper:
        required_chars.append(random.choice(upper_chars))
    if use_lower:
        required_chars.append(random.choice(lower_chars))
    if use_digits:
        required_chars.append(random.choice(digit_chars))
    if use_symbols:
        required_chars.append(random.choice(symbol_chars))

    remaining_length = max(length, len(custom_word) + len(required_chars)) - (len(custom_word) + len(required_chars))
    random_part = ''.join(random.choice(all_chars) for _ in range(remaining_length))
    
    final_password = custom_word + ''.join(required_chars) + random_part
    return final_password

length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
custom_word = input("Enter a word/number to include (or press Enter to skip): ")

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols, custom_word)
print(f"\nGenerated Password: {password}")
