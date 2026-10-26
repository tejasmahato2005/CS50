text = input("Text: ")

# Initialize counters
letters = 0
words = 1  # Start with 1 since last word won't have a space after it
sentences = 0

# Count letters, words, and sentences
for char in text:
    if char.isalpha():  # Count only alphabetic characters as letters
        letters += 1
    elif char == ' ':   # Count spaces to determine words
        words += 1
    elif char == '.' or char == '!' or char == '?':  # Count sentence endings
        sentences += 1

# Calculate Coleman-Liau index
# L = average number of letters per 100 words
# S = average number of sentences per 100 words
L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# Output the grade level
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
