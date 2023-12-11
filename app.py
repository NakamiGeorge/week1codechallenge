# Challenge 1: Converting 12-hour time to 24-hour time
def convert_to_24_hour_time(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}{minute:02d}"

# Challenge 2: Two numbers are positive
def two_numbers_positive(a, b, c):
    positive_count = sum(1 for num in [a, b, c] if num > 0)
    return positive_count == 2

# Challenge 3: Consonant value
def consonant_value(word):
    consonants = [char for char in word if char not in "aeiou"]
    values = [ord(char) - ord('a') + 1 for char in consonants]
    return sum(values)

# Test cases
print(f"Challenge 1: {convert_to_24_hour_time(8, 30, 'am')}")
print(f"Challenge 2: {two_numbers_positive(2, 4, -3)}")
print(f"Challenge 3: {consonant_value('zodiacs')}")
