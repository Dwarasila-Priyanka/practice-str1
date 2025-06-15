# 1. Print each character of a string on a new line.
text = "Python"
for i in text:
    print(i) #P y t h o n

#2.Count the number of vowels in a string.

text = "hello world"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count) #Vowel count: 3

# 3. Reverse a string without using slicing

text = "hello"
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text) # olleh


# 4. Check if a string is a palindrome

text = "madam"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

if text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome") # Palindrome

# 5. Print words longer than 3 characters.

text = "I love learning Python programming"
words = text.split()

for word in words:
    if len(word) > 3:
        print(word) # programming



