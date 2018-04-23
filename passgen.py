import random
import string
import copy
SPECIAL_CHARS = '!@#$%^&*()'
VOWELS_LIST = 'aeiou'

def select_chars(chars, selection):
    if selection > len(chars):
        raise RuntimeError(
            "Number of Character to choose is greater than number of characters provided")
    values = []
    for _ in range(selection):
        v = random.choice(chars)
        values.append(v)
        chars.remove(v)
    return values

def generate_base(length, convert_vowels, digits_limit):
    if digits_limit < convert_vowels:
        convert_vowels = digits_limit
    counter = 0
    generated_digits = 0
    base = []
    while counter < length:
        letter = random.choice(string.ascii_letters)
        if letter.lower() in VOWELS_LIST and generated_digits < convert_vowels:
            letter = random.choice(string.digits)
            generated_digits+=1
        else:
            counter +=1
        base.append(letter)
    return base, generated_digits


def generate(minimum_length=10, digits=2, special_chars=2, convert_vowels=1):
    values = []
    base, generated_digits = generate_base(minimum_length-digits-special_chars, convert_vowels,digits)
    values.extend(base) 
    values.extend(select_chars(list(SPECIAL_CHARS), special_chars))
    values.extend(select_chars(list(string.digits), digits-generated_digits))
    random.shuffle(values)
    return ''.join(values)
